def extract_sections(text):

    lines = text.split("\n")

    sections = []

    current_heading = None
    current_content = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if (
    line.isupper()
    and len(line.split()) <= 5
    and len(line) > 5
):

            if current_heading is not None:

                sections.append({
                    "heading": current_heading,
                    "content": "\n".join(current_content)
                })

            current_heading = line
            current_content = []

        else:
            current_content.append(line)

    if current_heading is not None:

        sections.append({
            "heading": current_heading,
            "content": "\n".join(current_content)
        })

    return sections