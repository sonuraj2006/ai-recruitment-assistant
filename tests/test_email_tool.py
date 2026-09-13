from backend.integrations.email_tool import EmailTool


tool = EmailTool()

result = tool.send_email(
    candidate_name="Sonu Raj",
    candidate_email="sonu@example.com",
    subject="Interview Invitation",
    message="Your interview has been scheduled."
)

print("Email Integration Test")
print("----------------------")
print("Candidate:", result["candidate_name"])
print("Email:", result["candidate_email"])
print("Subject:", result["subject"])
print("Message:", result["message"])
print("Status:", result["status"])
print("Platform:", result["platform"])

status = tool.get_email_status(
    result["candidate_email"]
)

print("\nEmail Status")
print("------------")
print("Email:", status["candidate_email"])
print("Status:", status["status"])