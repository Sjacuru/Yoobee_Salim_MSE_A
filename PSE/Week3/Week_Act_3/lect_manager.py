from database_lect import create_connection_lect
import sqlite3

def add_lecturer(lecturer_name, lecturer_email):
    conn = create_connection_lect()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturers (lecturer_name, lecturer_email) VALUES (?, ?)", (lecturer_name, lecturer_email))
        conn.commit()
        print(" Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print(" E-mail must be unique.")
    conn.close()

def view_lecturers():
    conn = create_connection_lect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers")
    rows = cursor.fetchall()
    conn.close()
    return rows
