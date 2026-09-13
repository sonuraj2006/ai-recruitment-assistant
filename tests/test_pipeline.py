from backend.database.database import (
    create_tables,
    add_candidate,
    get_candidates,
    update_candidate_status,
    get_candidates_by_status
)


create_tables()

add_candidate(
    name="Pipeline Test Candidate",
    email="pipeline@example.com",
    phone="9876543210",
    skills=["Python", "SQL", "FastAPI"],
    resume_text="Python developer",
    match_score=85,
    status="Applied"
)

candidates = get_candidates()

candidate_id = candidates[0][0]

update_candidate_status(
    candidate_id,
    "Shortlisted"
)

shortlisted = get_candidates_by_status("Shortlisted")

print("Candidate Pipeline Test")
print("-----------------------")

for candidate in shortlisted:
    print("Candidate:", candidate[1])
    print("Score:", candidate[5])
    print("Status:", candidate[6])