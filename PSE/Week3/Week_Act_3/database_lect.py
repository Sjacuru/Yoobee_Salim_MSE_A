import sqlite3

def create_connection_lect():
    conn = sqlite3.connect("lecturers.db")
    return conn

def create_lect_tb():
    conn = create_connection_lect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecturer_name TEXT NOT NULL,
            lecturer_email TEXT NOT NULL UNIQUE  
       )
   ''')
    conn.commit()
    conn.close()