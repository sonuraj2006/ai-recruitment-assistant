from backend.matching.matcher import (
    extract_job_requirements,
    match_candidate
)


job_description = """
We need a Python developer with SQL, FastAPI,
Machine Learning and Git experience.
"""

candidate_skills = [
    "python",
    "java",
    "sql",
    "machine learning",
    "git"
]


required_skills = extract_job_requirements(job_description)

result = match_candidate(
    candidate_skills,
    required_skills
)

print("Required Skills:", required_skills)
print("Candidate Skills:", candidate_skills)
print("Match Score:", result["score"])
print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])