from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(job_description, top_n=20):

    vectorizer = TfidfVectorizer(
        stop_words='english'
        
    )

    matrix = vectorizer.fit_transform(
        [job_description]
    )

    scores = zip(
        vectorizer.get_feature_names_out(),
        matrix.toarray()[0]
    )

    keywords = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    return [
        word for word, score in keywords[:top_n]
    ]