from app.resume_parser.parser import parse_resume


candidate = parse_resume("Sonu_Raj_Resume.pdf")

print("\n----- CANDIDATE INFORMATION -----")

print("Name:", candidate["name"])
print("Email:", candidate["email"])
print("Phone:", candidate["phone"])
print("Skills:", candidate["skills"])