class AssessmentTool:
    """
    Mock recruitment assessment tool.
    Simulates integration with a coding assessment platform
    such as HackerRank.
    """

    def create_assessment(self, candidate_name, candidate_email, job_role):
        assessment = {
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "job_role": job_role,
            "assessment_id": f"ASSESS-{candidate_name.replace(' ', '').upper()}",
            "status": "Created",
            "platform": "Mock Assessment Platform"
        }

        return assessment

    def get_assessment_status(self, assessment_id):
        return {
            "assessment_id": assessment_id,
            "status": "Pending"
        }