import sqlite3

def create_connection_clas():
    conn = sqlite3.connect("classes.db")
    return conn

def create_clas_tb(): 
    conn = create_connection_clas()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,          
            class_name TEXT NOT NULL UNIQUE
       )
   ''')
    conn.commit()
    conn.close()