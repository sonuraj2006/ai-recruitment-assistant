from backend.resume_parser.keyword_extractor import extract_skills


def extract_job_requirements(job_description):
    """
    Extract required skills from the job description.
    """

    required_skills = extract_skills(job_description)

    return required_skills


def match_candidate(candidate_skills, required_skills):
    """
    Compare candidate skills with job requirements.
    """

    candidate_skills = [skill.lower() for skill in candidate_skills]
    required_skills = [skill.lower() for skill in required_skills]

    if not required_skills:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched_skills = []

    for skill in required_skills:
        if skill in candidate_skills:
            matched_skills.append(skill)

    missing_skills = [
        skill for skill in required_skills
        if skill not in candidate_skills
    ]

    score = (len(matched_skills) / len(required_skills)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }