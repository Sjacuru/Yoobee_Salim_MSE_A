from database_clas import create_connection_clas
import sqlite3

def add_class(class_name):
    conn = create_connection_clas()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO classes (class_name) VALUES (?)", (class_name))
        conn.commit()
        print(" Class added successfully.")
    except sqlite3.IntegrityError:
        print(" Class name must be unique.")
    conn.close()

def view_classes():
    conn = create_connection_clas()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    rows = cursor.fetchall()
    conn.close()
    return rows
