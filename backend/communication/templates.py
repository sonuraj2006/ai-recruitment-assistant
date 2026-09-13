def interview_invitation(candidate_name, interview_date, interview_time):
    return f"""
Subject: Interview Invitation

Dear {candidate_name},

We are pleased to inform you that you have been shortlisted for an interview.

Interview Date: {interview_date}
Interview Time: {interview_time}

Please be available at the scheduled time.

We look forward to speaking with you.

Best regards,
Recruitment Team
"""


def shortlist_message(candidate_name):
    return f"""
Subject: Application Shortlisted

Dear {candidate_name},

Congratulations!

Your application has been shortlisted for the next stage of our recruitment process.

Our recruitment team will contact you with further details.

Best regards,
Recruitment Team
"""


def rejection_message(candidate_name):
    return f"""
Subject: Application Update

Dear {candidate_name},

Thank you for your interest in the position and for taking the time to apply.

After reviewing your application, we have decided not to proceed with your application at this time.

We appreciate your interest and wish you success in your future career.

Best regards,
Recruitment Team
"""


def interview_reminder(candidate_name, interview_date, interview_time):
    return f"""
Subject: Interview Reminder

Dear {candidate_name},

This is a reminder about your upcoming interview.

Interview Date: {interview_date}
Interview Time: {interview_time}

Please be available at the scheduled time.

Best regards,
Recruitment Team
"""