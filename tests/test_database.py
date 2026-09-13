from backend.database.database import (
    create_tables,
    add_candidate,
    get_candidates
)


create_tables()


add_candidate(
    name="Candidate A",
    email="candidatea@example.com",
    phone="9876543210",
    skills=["python", "sql", "git"],
    resume_text="Python developer with SQL and Git experience.",
    match_score=80
)


add_candidate(
    name="Candidate B",
    email="candidateb@example.com",
    phone="9876543211",
    skills=["python", "sql", "fastapi", "git"],
    resume_text="Python developer with FastAPI, SQL and Git experience.",
    match_score=95
)


candidates = get_candidates()


print("Candidates in Database")
print("----------------------")

for candidate in candidates:
    print(candidate)