from database_stud import create_connection_stud
import sqlite3

def add_student(student_name, student_email):
    conn = create_connection_stud()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_name, student_email) VALUES (?, ?)", (student_name, student_email))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" E-mail must be unique.")
    conn.close()

def view_students():
    conn = create_connection_stud()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows
