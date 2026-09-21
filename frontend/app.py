import streamlit as st

from backend.integrations.assessment_tool import AssessmentTool
from backend.integrations.email_tool import EmailTool

from backend.resume_parser import (
    extract_resume_text,
    extract_skills,
    extract_email,
    extract_phone,
    extract_name
)

from backend.matching.matcher import (
    extract_job_requirements,
    match_candidate
)

from backend.database.database import (
    create_tables,
    add_candidate,
    get_candidates,
    update_candidate_status,
    get_candidates_by_status
)

from backend.matching.ranking import rank_candidates

from backend.scheduling.scheduler import schedule_interview

from backend.communication.templates import (
    interview_invitation,
    shortlist_message,
    rejection_message,
    interview_reminder
)

from backend.candidate_details.notice_salary import (
    extract_notice_period,
    extract_salary_expectation,
    check_notice_period,
    check_salary_expectation
)

from backend.candidate_details.education import (
    recognize_education
)

from backend.candidate_details.location import (
    extract_location,
    extract_relocation_willingness,
    check_location_match
)


# Create database tables
create_tables()


# Page configuration
st.set_page_config(
    page_title="Recruiter AI Agent",
    page_icon="🤖",
    layout="wide"
)


# ------------------------------------------------
# Main heading
# ------------------------------------------------

st.title("🤖 Recruiter AI Agent")

st.subheader("Resume Screening Assistant")

st.write(
    "Upload a candidate resume and enter the job description "
    "to screen the candidate."
)


# ------------------------------------------------
# Resume upload
# ------------------------------------------------

resume_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)


# ------------------------------------------------
# Job description
# ------------------------------------------------

job_description = st.text_area(
    "💼 Enter Job Description",
    height=200,
    placeholder=(
        "Example: We are looking for a Python Developer "
        "with experience in SQL, FastAPI, Machine Learning and Git."
    )
)


# ------------------------------------------------
# Recruitment requirements
# ------------------------------------------------

st.subheader("Recruitment Requirements")

maximum_notice = st.number_input(
    "Maximum Notice Period (days)",
    min_value=0,
    max_value=180,
    value=60
)

minimum_salary = st.number_input(
    "Minimum Salary (LPA)",
    min_value=0.0,
    value=6.0
)

maximum_salary = st.number_input(
    "Maximum Salary (LPA)",
    min_value=0.0,
    value=10.0
)

job_location = st.text_input(
    "Job Location",
    value="Hyderabad"
)


# ------------------------------------------------
# Screen candidate
# ------------------------------------------------

if resume_file and job_description:

    if st.button("🔍 Screen Candidate"):

        try:

            # 1. Extract resume text
            resume_text = extract_resume_text(resume_file)

            notice_period = extract_notice_period(resume_text)
            expected_salary = extract_salary_expectation(resume_text)

            education = recognize_education(resume_text)

            candidate_location = extract_location(resume_text)
            relocation = extract_relocation_willingness(resume_text)

            if not resume_text.strip():

                st.error(
                    "Could not extract text from the resume."
                )

            else:

                st.success(
                    "✅ Resume successfully processed!"
                )

                # 2. Extract candidate information
                name = extract_name(resume_text)
                email = extract_email(resume_text)
                phone = extract_phone(resume_text)

                candidate_skills = extract_skills(
                    resume_text
                )


                # 3. Candidate information
                st.subheader(
                    "👤 Candidate Information"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write("**Name**")
                    st.write(name)

                with col2:
                    st.write("**Email**")
                    st.write(email)

                with col3:
                    st.write("**Phone**")
                    st.write(phone)


                # 4. Candidate skills
                st.subheader(
                    "🛠️ Candidate Skills"
                )

                if candidate_skills:

                    st.write(
                        ", ".join(candidate_skills)
                    )

                else:

                    st.write(
                        "No matching skills found."
                    )


                # 5. Job requirements
                required_skills = extract_job_requirements(
                    job_description
                )

                st.subheader(
                    "💼 Job Requirements"
                )

                if required_skills:

                    st.write(
                        ", ".join(required_skills)
                    )

                else:

                    st.warning(
                        "No matching skills were found "
                        "in the job description."
                    )


                # 6. Match candidate
                result = match_candidate(
                    candidate_skills,
                    required_skills
                )


                # 7. Match score
                st.subheader(
                    "📊 Candidate Match Score"
                )

                st.metric(
                    label="Match Score",
                    value=f"{result['score']}%"
                )


                # 8. Matched skills
                st.subheader(
                    "✅ Matched Skills"
                )

                if result["matched_skills"]:

                    st.write(
                        ", ".join(
                            result["matched_skills"]
                        )
                    )

                else:

                    st.write(
                        "No matched skills."
                    )


                # 9. Missing skills
                st.subheader(
                    "❌ Missing Skills"
                )

                if result["missing_skills"]:

                    st.write(
                        ", ".join(
                            result["missing_skills"]
                        )
                    )

                else:

                    st.write(
                        "No missing skills!"
                    )


                # 10. Candidate details
                st.subheader("Candidate Details")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(
                        "**Notice Period:**",
                        f"{notice_period} days"
                        if notice_period is not None
                        else "Not Available"
                    )

                    st.write(
                        "**Expected Salary:**",
                        f"{expected_salary} LPA"
                        if expected_salary is not None
                        else "Not Available"
                    )

                    st.write(
                        "**Education:**",
                        education["degree"]
                        if education["degree"]
                        else "Not Available"
                    )

                with col2:
                    st.write(
                        "**College:**",
                        education["college"]
                        if education["college"]
                        else "Not Available"
                    )

                    st.write(
                        "**Location:**",
                        candidate_location
                        if candidate_location
                        else "Not Available"
                    )

                    st.write(
                        "**Relocation Willingness:**",
                        relocation
                    )


                # 11. Requirement matching
                notice_result = check_notice_period(
                    notice_period,
                    maximum_notice
                )

                salary_result = check_salary_expectation(
                    expected_salary,
                    minimum_salary,
                    maximum_salary
                )

                location_result = check_location_match(
                    candidate_location,
                    job_location
                )

                st.subheader("Requirement Matching")

                st.write("**Notice Period:**", notice_result)
                st.write("**Salary Expectation:**", salary_result)
                st.write("**Location:**", location_result)
                st.write("**Relocation:**", relocation)


                # 12. Save candidate
                add_candidate(
                    name=name,
                    email=email,
                    phone=phone,
                    skills=candidate_skills,
                    resume_text=resume_text,
                    match_score=result["score"]
                )

                st.success(
                    "💾 Candidate information saved "
                    "to SQLite database."
                )


                # 13. Resume text
                with st.expander(
                    "📄 View Extracted Resume Text"
                ):

                    st.write(resume_text)


        except Exception as e:

            st.error(
                f"Error processing resume: {e}"
            )


# ------------------------------------------------
# Candidate ranking
# ------------------------------------------------

st.divider()

st.header(
    "🏆 Candidate Ranking"
)

st.write(
    "Candidates are ranked based on their "
    "resume match score."
)


try:

    database_candidates = get_candidates()

    if database_candidates:

        candidates = []

        for candidate in database_candidates:

            candidates.append(
                {
                    "id": candidate[0],
                    "name": candidate[1],
                    "email": candidate[2],
                    "phone": candidate[3],
                    "skills": candidate[4],
                    "score": candidate[5]
                }
            )


        # Rank candidates
        ranked_candidates = rank_candidates(
            candidates
        )


        # Create table
        ranking_data = []

        for candidate in ranked_candidates:

            ranking_data.append(
                {
                    "Rank": candidate["rank"],
                    "Name": candidate["name"],
                    "Email": candidate["email"],
                    "Phone": candidate["phone"],
                    "Skills": candidate["skills"],
                    "Match Score": (
                        f'{candidate["score"]}%'
                    )
                }
            )

        st.dataframe(
            ranking_data,
            use_container_width=True
        )


    else:

        st.info(
            "No candidates have been screened yet."
        )


except Exception as e:

    st.error(
        f"Could not load candidate ranking: {e}"
    )


# ------------------------------------------------
# Interview Scheduling
# ------------------------------------------------

st.divider()

st.header("📅 Interview Scheduling")

st.write(
    "Schedule an interview for a candidate."
)


candidate_name = st.text_input(
    "Candidate Name"
)

candidate_email = st.text_input(
    "Candidate Email"
)

interview_date = st.date_input(
    "Interview Date"
)

interview_time = st.time_input(
    "Interview Time"
)

interview_type = st.selectbox(
    "Interview Type",
    [
        "Online",
        "In-person",
        "Phone"
    ]
)


if st.button("📅 Schedule Interview"):

    try:

        result = schedule_interview(
            candidate_name=candidate_name,
            candidate_email=candidate_email,
            interview_date=interview_date.strftime("%Y-%m-%d"),
            interview_time=interview_time.strftime("%H:%M"),
            interview_type=interview_type
        )

        st.success(
            "✅ Interview scheduled successfully!"
        )

        st.write(
            "**Candidate:**",
            result["candidate_name"]
        )

        st.write(
            "**Email:**",
            result["candidate_email"]
        )

        st.write(
            "**Date:**",
            result["interview_date"]
        )

        st.write(
            "**Time:**",
            result["interview_time"]
        )

        st.write(
            "**Type:**",
            result["interview_type"]
        )

        st.write(
            "**Status:**",
            result["status"]
        )

    except Exception as e:

        st.error(
            f"Could not schedule interview: {e}"
        )


# ------------------------------------------------
# Communication Templates
# ------------------------------------------------

st.divider()

st.header("✉️ Communication Templates")

st.write(
    "Generate professional communication messages "
    "for candidates."
)


communication_type = st.selectbox(
    "Select Communication Type",
    [
        "Interview Invitation",
        "Shortlist Message",
        "Rejection Message",
        "Interview Reminder"
    ]
)


communication_candidate = st.text_input(
    "Candidate Name",
    key="communication_candidate"
)


if communication_type in [
    "Interview Invitation",
    "Interview Reminder"
]:

    communication_date = st.date_input(
        "Interview Date",
        key="communication_date"
    )

    communication_time = st.time_input(
        "Interview Time",
        key="communication_time"
    )


if st.button("✉️ Generate Message"):

    if not communication_candidate.strip():

        st.warning(
            "Please enter the candidate name."
        )

    else:

        if communication_type == "Interview Invitation":

            message = interview_invitation(
                communication_candidate,
                communication_date.strftime("%Y-%m-%d"),
                communication_time.strftime("%H:%M")
            )


        elif communication_type == "Shortlist Message":

            message = shortlist_message(
                communication_candidate
            )


        elif communication_type == "Rejection Message":

            message = rejection_message(
                communication_candidate
            )


        else:

            message = interview_reminder(
                communication_candidate,
                communication_date.strftime("%Y-%m-%d"),
                communication_time.strftime("%H:%M")
            )


        st.success(
            "✅ Communication message generated!"
        )

        st.text_area(
            "Generated Message",
            message,
            height=300
        )


# ------------------------------------------------
# Candidate Assessment
# ------------------------------------------------

st.divider()

st.header("💻 Candidate Assessment")

st.write("Create a coding assessment for a shortlisted candidate.")

assessment_candidate = st.text_input(
    "Candidate Name",
    key="assessment_candidate"
)

assessment_email = st.text_input(
    "Candidate Email",
    key="assessment_email"
)

assessment_job = st.text_input(
    "Job Role",
    key="assessment_job"
)

if st.button("💻 Create Assessment"):

    if not assessment_candidate or not assessment_email or not assessment_job:
        st.warning("Please fill all assessment details.")

    else:
        assessment_tool = AssessmentTool()

        result = assessment_tool.create_assessment(
            candidate_name=assessment_candidate,
            candidate_email=assessment_email,
            job_role=assessment_job
        )

        st.success("✅ Assessment created successfully!")

        st.write("**Candidate:**", result["candidate_name"])
        st.write("**Email:**", result["candidate_email"])
        st.write("**Job Role:**", result["job_role"])
        st.write("**Assessment ID:**", result["assessment_id"])
        st.write("**Status:**", result["status"])
        st.write("**Platform:**", result["platform"])


# ------------------------------------------------
# Recruitment Email
# ------------------------------------------------

st.divider()

st.header("📧 Recruitment Email")

st.write("Send a recruitment communication to a candidate.")

email_candidate = st.text_input(
    "Candidate Name",
    key="email_candidate"
)

email_address = st.text_input(
    "Candidate Email",
    key="email_address"
)

email_subject = st.text_input(
    "Email Subject",
    value="Interview Invitation",
    key="email_subject"
)

email_message = st.text_area(
    "Email Message",
    value="Your interview has been scheduled.",
    key="email_message"
)

if st.button("📧 Send Recruitment Email"):

    if not email_candidate or not email_address or not email_subject or not email_message:
        st.warning("Please fill all email details.")

    else:
        email_tool = EmailTool()

        result = email_tool.send_email(
            candidate_name=email_candidate,
            candidate_email=email_address,
            subject=email_subject,
            message=email_message
        )

        st.success("✅ Recruitment email sent successfully!")

        st.write("**Candidate:**", result["candidate_name"])
        st.write("**Email:**", result["candidate_email"])
        st.write("**Subject:**", result["subject"])
        st.write("**Message:**", result["message"])
        st.write("**Status:**", result["status"])
        st.write("**Platform:**", result["platform"])


# ------------------------------------------------
# Candidate Pipeline
# ------------------------------------------------

st.divider()

st.header("📊 Candidate Pipeline")

pipeline_candidates = get_candidates()

for candidate in pipeline_candidates:

    candidate_id = candidate[0]
    candidate_name = candidate[1]
    candidate_email = candidate[2]
    match_score = candidate[5]
    current_status = candidate[6]

    st.write("###", candidate_name)
    st.write("Email:", candidate_email)
    st.write("Match Score:", f"{match_score}%")
    st.write("Current Status:", current_status)

    statuses = [
        "Applied",
        "Shortlisted",
        "Assessment",
        "Interview",
        "Selected",
        "Rejected"
    ]

    new_status = st.selectbox(
        "Status",
        statuses,
        index=statuses.index(current_status),
        key=f"pipeline_status_{candidate_id}"
    )

    if st.button(
        "Update Candidate Status",
        key=f"pipeline_update_{candidate_id}"
    ):
        update_candidate_status(
            candidate_id,
            new_status
        )

        st.success(
            f"✅ {candidate_name} status updated to {new_status}"
        )

        st.rerun()
