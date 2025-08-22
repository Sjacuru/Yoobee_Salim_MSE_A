import sqlite3

def create_connection_stud():
    conn = sqlite3.connect("students.db")
    return conn

def create_stud_tb():
    conn = create_connection_stud()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_email TEXT NOT NULL UNIQUE
       )
   ''')
    conn.commit()
    conn.close()