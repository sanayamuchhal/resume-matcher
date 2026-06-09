def compare_keywords(
    resume_text,
    keywords
):

    resume_text = resume_text.lower()

    matched = []
    missing = []

    for keyword in keywords:

        if keyword.lower() in resume_text:
            matched.append(keyword)
        else:
            missing.append(keyword)

    return matched, missing