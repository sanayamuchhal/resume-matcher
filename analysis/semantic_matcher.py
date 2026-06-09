from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def semantic_match(resume_text, job_description):

    resume_chunks = [
        line.strip()
        for line in resume_text.split("\n")
        if len(line.strip()) > 20
    ]

    jd_chunks = [
        line.strip()
        for line in job_description.split(".")
        if len(line.strip()) > 10
    ]

    if not resume_chunks or not jd_chunks:
        return 0

    resume_embeddings = model.encode(
        resume_chunks
    )

    jd_embeddings = model.encode(
        jd_chunks
    )

    scores = []

    for jd_embedding in jd_embeddings:

        similarities = cosine_similarity(
            [jd_embedding],
            resume_embeddings
        )[0]

        best_score = max(similarities)

        scores.append(best_score)

    
    scores.sort(reverse=True)

    top_k = min(5, len(scores))

    top_scores = scores[:top_k]

    return round(
        (sum(top_scores) / len(top_scores)) * 100,
        2
    )