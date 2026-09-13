from backend.communication.templates import (
    interview_invitation,
    shortlist_message,
    rejection_message,
    interview_reminder
)


print("Communication Templates Test")
print("============================")


print("\n--- Interview Invitation ---")

print(
    interview_invitation(
        "Sonu Raj",
        "2026-09-20",
        "10:30"
    )
)


print("\n--- Shortlist Message ---")

print(
    shortlist_message(
        "Sonu Raj"
    )
)


print("\n--- Rejection Message ---")

print(
    rejection_message(
        "Sonu Raj"
    )
)


print("\n--- Interview Reminder ---")

print(
    interview_reminder(
        "Sonu Raj",
        "2026-09-20",
        "10:30"
    )
)