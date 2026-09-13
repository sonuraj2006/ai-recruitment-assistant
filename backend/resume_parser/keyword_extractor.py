import re


SKILLS = [
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "scikit-learn",
    "javascript",
    "node.js",
    "tensorflow",
    "pytorch",
    "streamlit",
    "langchain",
    "fastapi",
    "django",
    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "react",
    "pandas",
    "numpy",
    "aws",
    "azure",
    "docker",
    "github",
    "git",
    "c"
]


def extract_skills(text):
    """
    Extract technical skills from text.
    Uses whole-word matching to avoid false matches.
    """

    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters such as + and .
        escaped_skill = re.escape(skill.lower())

        # Match complete words/phrases
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills


def extract_email(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):
    pattern = r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_name(text):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        return lines[0]

    return None