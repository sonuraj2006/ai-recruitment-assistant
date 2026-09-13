import sqlite3


DATABASE_NAME = "recruitment.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            resume_text TEXT,
            match_score REAL
        )
    """)

    connection.commit()
    connection.close()


def add_candidate(
    name,
    email,
    phone,
    skills,
    resume_text,
    match_score
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO candidates
        (name, email, phone, skills, resume_text, match_score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        email,
        phone,
        ", ".join(skills),
        resume_text,
        match_score
    ))

    connection.commit()
    connection.close()


def get_candidates():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, phone, skills, match_score
        FROM candidates
        ORDER BY match_score DESC
    """)

    candidates = cursor.fetchall()

    connection.close()

    return candidates