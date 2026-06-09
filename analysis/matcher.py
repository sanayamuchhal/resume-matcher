from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


def match_resumes(resume_text, job_description):

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer(ngram_range=(1,2))

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    match_percentage = similarity[0][0] * 100

    return round(match_percentage, 2)