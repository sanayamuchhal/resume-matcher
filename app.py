from flask import Flask, render_template, request

from parser.extract import extract_text
from analysis.matcher import match_resumes

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        resume = request.files['resume']

        job_description = request.form['job_description']

        pdf_path = 'uploads/' + resume.filename

        resume.save(pdf_path)

        resume_text = extract_text(pdf_path)

        match_score = match_resumes(resume_text, job_description)

        return render_template(
            'index.html',
            score=match_score
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)