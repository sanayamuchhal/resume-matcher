def extract_requirements(job_description):

    lines = job_description.split("\n")

    requirements = []

    triggers = [
        "knowledge",
        "experience",
        "understanding",
        "proficiency",
        "familiarity",
        "ability",
        "skills"
    ]

    for line in lines:

        line = line.strip()

        if len(line) < 10:
            continue

        lower = line.lower()

        if any(word in lower for word in triggers):

            line = line.replace("*", "")
            line = line.replace("-", "")
            

            requirements.append(line)

    return requirements


def generate_questions(requirements):

    questions = []

    for req in requirements:

        questions.append(
            f"Do you have experience or knowledge related to: {req}?"
        )

    return questions