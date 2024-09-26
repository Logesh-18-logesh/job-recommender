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

> /flask_app/
│
├── /templates/
│   ├── index.html
│   └── result.html
│
├── app.py
└── job_descriptions.xlsx


3. Run the app.py file


## HOW THE CODE WORKS: ##

1. Gets the student details

2. Finds the similarity score between the skills using TF-IDF VECTORIZER and cosine similarity

3. Displays the recommended jobs based on the similarity score and the conditions that satisfies the company's requirements  
