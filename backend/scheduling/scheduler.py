from datetime import datetime


def schedule_interview(
    candidate_name,
    candidate_email,
    interview_date,
    interview_time,
    interview_type="Online"
):
    """
    Create an interview schedule for a candidate.
    """

    # Combine date and time
    interview_datetime = datetime.strptime(
        f"{interview_date} {interview_time}",
        "%Y-%m-%d %H:%M"
    )

    return {
        "candidate_name": candidate_name,
        "candidate_email": candidate_email,
        "interview_date": interview_datetime.strftime("%Y-%m-%d"),
        "interview_time": interview_datetime.strftime("%H:%M"),
        "interview_type": interview_type,
        "status": "Scheduled"
    }