import re


DEGREES = [
    "B.Tech",
    "B.E",
    "M.Tech",
    "M.E",
    "B.Sc",
    "M.Sc",
    "BCA",
    "MCA"
]


def extract_degree(text):
    text_lower = text.lower()

    for degree in DEGREES:
        if degree.lower() in text_lower:
            return degree

    return None


def extract_college(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:
        if any(word in line.lower() for word in [
            "college",
            "institute",
            "university"
        ]):
            return line

    return None


def recognize_education(text):
    degree = extract_degree(text)
    college = extract_college(text)

    return {
        "degree": degree,
        "college": college
    }