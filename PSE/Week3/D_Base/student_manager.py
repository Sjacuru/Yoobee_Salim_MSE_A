from database_stu import create_connection_stu
import sqlite3

def add_student(student_name, student_mail, stu_Address):
    conn = create_connection_stu()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_name, student_mail, stu_Address) VALUES (?, ?, ?)", (student_name, student_mail , stu_Address))
        conn.commit()
        print(" student added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_students():
    conn = create_connection_stu()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(student_name):
    conn = create_connection_stu()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + student_name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection_stu()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️  User deleted.")