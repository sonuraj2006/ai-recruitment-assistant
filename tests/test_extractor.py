from app.resume_parser.extractor import extract_resume_text


text = extract_resume_text("Sonu_Raj_Resume.pdf")

print("----- EXTRACTED RESUME TEXT -----")
print(text)