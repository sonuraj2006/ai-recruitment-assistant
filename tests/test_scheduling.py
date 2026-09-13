from backend.scheduling.scheduler import schedule_interview


result = schedule_interview(
    candidate_name="Sonu Raj",
    candidate_email="sonu@example.com",
    interview_date="2026-09-20",
    interview_time="10:30",
    interview_type="Online"
)


print("Interview Scheduling Test")
print("-------------------------")
print("Candidate:", result["candidate_name"])
print("Email:", result["candidate_email"])
print("Date:", result["interview_date"])
print("Time:", result["interview_time"])
print("Type:", result["interview_type"])
print("Status:", result["status"])