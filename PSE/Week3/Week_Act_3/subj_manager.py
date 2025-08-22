from database_subj import create_connection_subj
import sqlite3

def add_subject(subject_name, subject_desc):
    conn = create_connection_subj()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (subject_name, subject_desc) VALUES (?, ?)", (subject_name, subject_desc))
        conn.commit()
        print(" subject added successfully.")
    except sqlite3.IntegrityError:
        print(" Subject name must be unique.")
    conn.close()

def view_subjects():
    conn = create_connection_subj()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    rows = cursor.fetchall()
    conn.close()
    return rows
