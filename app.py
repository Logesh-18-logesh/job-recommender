from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# Load job data from Excel file
df = pd.read_excel(r"D:\websort\sorting\job_descriptions.xlsx") #add the path of the dataset downloaded from the kaggle 

# Helper function to parse experience range
def parse_experience_range(exp_str):
    match = re.match(r"(\d+)\s*to\s*(\d+)\s*Years", exp_str)
    if match:
        min_exp, max_exp = int(match.group(1)), int(match.group(2))
        return min_exp, max_exp
    else:
        match = re.match(r"(\d+)\s*Years", exp_str)
        if match:
            return int(match.group(1)), int(match.group(1))
    return None, None

# Check if student's experience matches the job's experience range
def is_experience_match(student_exp, job_exp_str):
    min_exp, max_exp = parse_experience_range(job_exp_str)
    if min_exp is not None and max_exp is not None:
        return min_exp <= student_exp <= max_exp
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect student data from the form
    student_data = {
        'name': request.form['name'],
        'skills': request.form['skills'],
        'cgpa': float(request.form['cgpa']),
        'qualification': request.form['qualification'],
        'gender': request.form['gender'],
        'Work type': request.form['work_type'],
        'experience': int(request.form['experience'])
    }

    # Combine student skills with job skills for TF-IDF vectorization
    all_skills = [student_data['skills']] + list(df['skills'])
    vectorizer = TfidfVectorizer()
    skills_matrix = vectorizer.fit_transform(all_skills)

    student_skills_vector = skills_matrix[0]
    job_skills_matrix = skills_matrix[1:]
    similarity_scores = cosine_similarity(student_skills_vector, job_skills_matrix).flatten()

    # Add similarity scores to the DataFrame
    df['similarity_score'] = similarity_scores

    # Match experience
    df['experience_match'] = df['Experience'].apply(lambda x: is_experience_match(student_data['experience'], x))

    # Filter companies that match the student's CGPA, degree, work type, gender preference, and experience
    filtered_jobs = df[
        (df['CGPA'] <= student_data['cgpa']) &
        (df['Qualifications'] == student_data['qualification']) &
        (df['Work Type'] == student_data['Work type']) &
        ((df['Preference'] == student_data['gender']) | (df['Preference'] == 'Both')) &
        (df['experience_match'] == True)
    ]

    # Sort the jobs by similarity score in descending order
    recommended_jobs = filtered_jobs.loc[filtered_jobs['similarity_score'] != 0]
    recommended_jobs = recommended_jobs.sort_values(by='similarity_score', ascending=False)

    # Get job information: Job Id, Company, Job Role, Similarity Score, and Link
    job_info = recommended_jobs[['Job Id', 'Company', 'Job Title', 'similarity_score', 'Link']].to_dict(orient='records')

    # Render the result template with the recommended jobs
    return render_template('result.html', jobs=job_info)

if __name__ == '__main__':
    app.run(debug=True)
