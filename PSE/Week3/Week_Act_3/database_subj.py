import sqlite3

def create_connection_subj():
    conn = sqlite3.connect("subjects.db")
    return conn

def create_subj_tb(): 
    conn = create_connection_subj()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,          
            subject_name TEXT NOT NULL UNIQUE,
            subject_desc TEXT NOT NULL
       )
   ''')
    conn.commit()
    conn.close()