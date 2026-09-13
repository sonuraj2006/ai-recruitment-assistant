from app.resume_parser.extractor import extract_resume_text
from app.resume_parser.keyword_extractor import extract_skills


text = extract_resume_text("Sonu_Raj_Resume.pdf")

skills = extract_skills(text)

print("----- EXTRACTED SKILLS -----")

for skill in skills:
    print("-", skill)