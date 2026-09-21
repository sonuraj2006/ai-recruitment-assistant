from backend.candidate_details.notice_salary import (
    extract_notice_period,
    extract_salary_expectation,
    check_notice_period,
    check_salary_expectation
)


resume_text = """
Sonu Raj
Python Developer
Expected Salary: 8 LPA
Notice Period: 30 days
"""

notice_period = extract_notice_period(resume_text)
salary = extract_salary_expectation(resume_text)

notice_result = check_notice_period(
    notice_period,
    60
)

salary_result = check_salary_expectation(
    salary,
    6,
    10
)

print("Notice Period & Salary Test")
print("----------------------------")
print("Notice Period:", notice_period, "days")
print("Notice Result:", notice_result)
print("Expected Salary:", salary, "LPA")
print("Salary Result:", salary_result)