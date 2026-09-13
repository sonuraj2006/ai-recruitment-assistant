from backend.resume_parser.extractor import extract_resume_text
from backend.resume_parser.keyword_extractor import (
    extract_skills,
    extract_email,
    extract_phone,
    extract_name
)


def parse_resume(file_path):

    text = extract_resume_text(file_path)

    candidate = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "resume_text": text
    }

    return candidate