import sqlite3

def explore_database():
    """Complete exploration of the database"""
    conn = sqlite3.connect("Mydatabase.db")
    cursor = conn.cursor()
    
    print("=== DATABASE EXPLORER ===\n")
    
    # 1. List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    
    print("Tables found:", tables)
    
    # 2. Explore each table
    for table in tables:
        print(f"\n--- Exploring table: {table} ---")
        
        # Get column info
        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()
        print("Columns:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"Total rows: {count}")
        
        # Show first few rows
        if count > 0:
            cursor.execute(f"SELECT * FROM {table} LIMIT 5")
            rows = cursor.fetchall()
            print("Sample data:")
            for row in rows:
                print(f"  {row}")
    
    conn.close()

# Run the explorer
explore_database()

