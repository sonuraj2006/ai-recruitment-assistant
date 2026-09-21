import re


def extract_notice_period(text):
    text_lower = text.lower()

    if "immediate joiner" in text_lower or "immediate joining" in text_lower:
        return 0

    patterns = [
        r'(\d+)\s*days?\s*notice',
        r'(\d+)\s*days?\s*notice\s*period',
        r'notice\s*period\s*[:\-]?\s*(\d+)\s*days?',
        r'(\d+)\s*months?\s*notice',
        r'(\d+)\s*months?\s*notice\s*period'
    ]

    for pattern in patterns:
        match = re.search(pattern, text_lower)

        if match:
            value = int(match.group(1))

            if "month" in match.group(0):
                return value * 30

            return value

    return None


def extract_salary_expectation(text):
    text_lower = text.lower()

    patterns = [
        r'expected salary\s*[:\-]?\s*(?:₹|rs\.?|inr)?\s*(\d+(?:\.\d+)?)\s*(lpa|lakhs?|lakh)?',
        r'salary expectation\s*[:\-]?\s*(?:₹|rs\.?|inr)?\s*(\d+(?:\.\d+)?)\s*(lpa|lakhs?|lakh)?',
        r'expected ctc\s*[:\-]?\s*(?:₹|rs\.?|inr)?\s*(\d+(?:\.\d+)?)\s*(lpa|lakhs?|lakh)?'
    ]

    for pattern in patterns:
        match = re.search(pattern, text_lower)

        if match:
            salary = float(match.group(1))

            if match.group(2):
                salary *= 1

            return salary

    return None


def check_notice_period(candidate_days, maximum_days):
    if candidate_days is None:
        return "Not Available"

    if candidate_days <= maximum_days:
        return "Matches"

    return "Does Not Match"


def check_salary_expectation(candidate_salary, minimum_salary, maximum_salary):
    if candidate_salary is None:
        return "Not Available"

    if minimum_salary <= candidate_salary <= maximum_salary:
        return "Matches"

    if candidate_salary < minimum_salary:
        return "Below Range"

    return "Above Range"