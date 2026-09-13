class HackerEarthIntegration:
    """
    HackerEarth assessment integration layer.

    Currently uses a mock implementation.
    The API request can be added later when
    HackerEarth API credentials are available.
    """

    def create_assessment(
        self,
        candidate_name,
        candidate_email,
        job_role
    ):
        assessment_id = (
            f"HE-{candidate_name.replace(' ', '').upper()}"
        )

        return {
            "assessment_id": assessment_id,
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "job_role": job_role,
            "status": "Created",
            "platform": "HackerEarth"
        }

    def get_assessment_status(self, assessment_id):
        return {
            "assessment_id": assessment_id,
            "status": "Pending"
        }