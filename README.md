# Resume Matcher

A Flask-based NLP web application that compares a candidate's resume against a job description and generates a match score based on textual similarity.

## Overview

Recruiters often evaluate resumes by checking how closely they align with job requirements. This project automates that process by extracting text from PDF resumes and comparing it with a job description using Natural Language Processing (NLP) techniques.

The application calculates a similarity score using TF-IDF vectorization and cosine similarity and displays the result through a web interface.

---

## Features

* Upload resumes in PDF format
* Extract text from resumes automatically
* Paste any job description
* Generate a resume-job match score
* Dynamic score rendering using Flask and Jinja
* Modular project architecture

---

## Tech Stack

### Backend

* Python
* Flask

### NLP

* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

### PDF Processing

* pdfplumber

### Frontend

* HTML
* Jinja Templating

### Version Control

* Git
* GitHub

---

## Project Architecture

User Uploads Resume + Job Description

↓

Flask Backend

↓

PDF Text Extraction (pdfplumber)

↓

TF-IDF Vectorization

↓

Cosine Similarity Calculation

↓

Match Score Generation

↓

Result Displayed on Webpage

---

## Project Structure

resume-matcher/

├── app.py

├── analysis/

│ └── matcher.py

├── parser/

│ └── extract.py

├── templates/

│ └── index.html

├── requirements.txt

└── README.md

---

## How It Works

### Step 1: Resume Upload

The user uploads a PDF resume and enters a job description.

### Step 2: Text Extraction

The application extracts text from the uploaded PDF using pdfplumber.

### Step 3: Vectorization

The resume and job description are converted into numerical vectors using TF-IDF.

### Step 4: Similarity Analysis

Cosine similarity is used to compare the vectors and calculate a similarity score.

### Step 5: Result Generation

The similarity score is converted into a percentage and displayed on the webpage.

---

## Concepts Demonstrated

* Flask Web Development
* Frontend-Backend Integration
* File Upload Handling
* PDF Parsing
* Natural Language Processing
* TF-IDF Vectorization
* Cosine Similarity
* Jinja Templating
* Modular Software Design
* Git & GitHub Workflow

---

## Challenges Faced

* Understanding Flask routing and request handling
* Managing Python virtual environments
* Extracting text from PDF files
* Connecting backend logic with frontend templates
* Debugging package and dependency issues
* Learning Git and GitHub workflow

---

## Future Improvements

* Matched Skills Analysis
* Missing Skills Detection
* Resume Improvement Suggestions
* Better UI/UX Design
* Progress Bars and Analytics
* Database Integration
* Semantic Similarity using Sentence Transformers
* Multi-Job Comparison
* AI-Powered Resume Feedback

---

## Author

Sanaya Muchhal

B.Tech Computer Science Engineering

Manipal University Jaipur
