from flask import Flask, render_template, request

from parser.extract import extract_text
from analysis.matcher import match_resumes
from analysis.semantic_matcher import semantic_match
from analysis.section_parser import extract_sections
from analysis.keywords import extract_keywords
from analysis.skill_match import compare_keywords
from analysis.question_generator import (extract_requirements,generate_questions)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        resume = request.files['resume']
        job_description = request.form['job_description']

        pdf_path = 'uploads/' + resume.filename
        resume.save(pdf_path)

        
        resume_text = extract_text(pdf_path)

        
        keywords = extract_keywords(job_description)

        matched, missing = compare_keywords(
            resume_text,
            keywords
        )

        tfidf_score = match_resumes(
            resume_text,
            job_description
        )

        semantic_score = semantic_match(
            resume_text,
            job_description
        )

    

        sections = extract_sections(resume_text)

        section_results = []

        for section in sections:

            score = semantic_match(
                section["content"],
                job_description
            )

            section_results.append({
                "heading": section["heading"],
                "score": score,
                "content": section["content"][:300]
            })

       

        requirements = extract_requirements(
            job_description
        )

        questions = generate_questions(
            requirements
        )

        question_results = []

        for question in questions:

            best_score = 0
            best_section = "No evidence found"

            for section in sections:

                score = semantic_match(
                    section["content"],
                    question
                )

                if score > best_score:

                    best_score = score
                    best_section = section["heading"]

            question_results.append({
                "question": question,
                "score": round(best_score, 2),
                "evidence": best_section
            })

        return render_template(
            'index.html',
            tfidf_score=tfidf_score,
            semantic_score=semantic_score,
            matched=matched,
            missing=missing,
            section_results=section_results,
            question_results=question_results
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)