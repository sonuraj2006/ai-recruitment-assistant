from backend.integrations.hackerearth import HackerEarthIntegration


tool = HackerEarthIntegration()

result = tool.create_assessment(
    candidate_name="Sonu Raj",
    candidate_email="sonu@example.com",
    job_role="Python Developer"
)

print("HackerEarth Integration Test")
print("----------------------------")
print("Candidate:", result["candidate_name"])
print("Email:", result["candidate_email"])
print("Job Role:", result["job_role"])
print("Assessment ID:", result["assessment_id"])
print("Status:", result["status"])
print("Platform:", result["platform"])

status = tool.get_assessment_status(
    result["assessment_id"]
)

print("\nAssessment Status")
print("-----------------")
print("Assessment ID:", status["assessment_id"])
print("Status:", status["status"])