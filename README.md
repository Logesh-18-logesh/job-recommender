# WEBSORT JOB-RECOMMENDER
 This recommender uses TF-IDF vectorizer and cosine similarity to match the student's skills and the job's required skills and sort according to the similarity score and recommend the jobs which only satisfies the condition of the company's requirements.

 The data is all given by the excel sheet as input

## DATASET
  https://www.kaggle.com/datasets/logeshsd24/job-description-websort/data

make sure the dataset is in the above format and the dataset is stored in the same directory of app.py

## HOW TO RUN THE FILE 

1.Install the required libraries:
    
    > Flask

    > pandas
    
    > scikit-learn


2.Make sure you have all the contents in the directory as follows:

     > /your-directory/
 
     > │
  
     > ├── /templates/
  
     > │    ├── index.html
  
     > │    └── result.html
  
     > │
  
     > ├── app.py
  
     > └── job_descriptions.xlsx


3. Run the app.py file


## HOW THE CODE WORKS: ##

1. The user submits their information through the form on the index.html page.

2. The backend (app.py) processes the form data, calculates similarity scores using the TF-IDF algorithm, and checks the experience matching.

3. The backend filters and sorts the recommended jobs and passes the data to the result.html template.

4. The result page displays the recommended jobs in a table, each with a "View Job" button that, when clicked, navigates to the job's URL in a new tab.
