from backend.candidate_details.location import (
    extract_location,
    extract_relocation_willingness,
    check_location_match
)


resume_text = """
Sonu Raj
Hyderabad
Willing to relocate for the right opportunity.
"""

candidate_location = extract_location(resume_text)
relocation = extract_relocation_willingness(resume_text)

location_result = check_location_match(
    candidate_location,
    "Hyderabad"
)

print("Regional Preference & Relocation Test")
print("--------------------------------------")
print("Candidate Location:", candidate_location)
print("Relocation Willingness:", relocation)
print("Location Match:", location_result)