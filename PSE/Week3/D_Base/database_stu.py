import sqlite3

def create_connection_stu():
    conn = sqlite3.connect("students.db")
    return conn

def student_table():
    conn = create_connection_stu()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_mail TEXT NOT NULL UNIQUE,
            stu_Address TEXT NOT NULL 
       )
   ''')
    conn.commit()
    conn.close()