class EmailTool:
    """
    Mock email integration for recruitment communication.
    Simulates sending recruitment emails to candidates.
    """

    def send_email(self, candidate_name, candidate_email, subject, message):
        return {
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "subject": subject,
            "message": message,
            "status": "Sent",
            "platform": "Mock Email Service"
        }

    def get_email_status(self, candidate_email):
        return {
            "candidate_email": candidate_email,
            "status": "Delivered"
        }