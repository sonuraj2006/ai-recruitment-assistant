from backend.candidate_details.education import recognize_education


resume_text = """
Sonu Raj
B.Tech Computer Science and Engineering
MLR Institute of Technology
Hyderabad
"""

result = recognize_education(resume_text)

print("Indian Education Recognition Test")
print("----------------------------------")
print("Degree:", result["degree"])
print("College:", result["college"])