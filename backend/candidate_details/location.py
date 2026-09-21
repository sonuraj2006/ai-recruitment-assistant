import re


INDIAN_CITIES = [
    "Hyderabad",
    "Bangalore",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi",
    "Gurgaon",
    "Noida",
    "Kolkata",
    "Ahmedabad"
]


def extract_location(text):
    text_lower = text.lower()

    for city in INDIAN_CITIES:
        if city.lower() in text_lower:
            return city

    return None


def extract_relocation_willingness(text):
    text_lower = text.lower()

    if any(phrase in text_lower for phrase in [
        "willing to relocate",
        "open to relocation",
        "ready to relocate",
        "willingness to relocate"
    ]):
        return "Yes"

    if any(phrase in text_lower for phrase in [
        "not willing to relocate",
        "not open to relocation",
        "cannot relocate",
        "unwilling to relocate"
    ]):
        return "No"

    return "Not Available"


def check_location_match(candidate_location, job_location):
    if not candidate_location or not job_location:
        return "Not Available"

    if candidate_location.lower() == job_location.lower():
        return "Matches"

    return "Different Location"