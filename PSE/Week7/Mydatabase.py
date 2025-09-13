import sqlite3

def create_database_and_tables():
    conn = sqlite3.connect("Mydatabase.db")
    cursor = conn.cursor()

    #Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    ''')
    
    # Samples
    users_data = [
        (1, 'Salim', 'sal@example'),
        (2, 'Henrique', 'henr@example'),
        (3, 'Daniel', 'dan@example')
    ]
    
    cursor.executemany('''
    INSERT OR IGNORE INTO users (user_id, username, email)
    VALUES (?, ?, ?)
    ''', users_data)
    
    # Insert sample data into orders table
    orders_data = [
        (1, 1, 'Computer', 1, 999.99),
        (2, 1, 'Mouse', 2, 49.99),
        (3, 2, 'Keyboard', 1, 79.99),
        (4, 2, 'Monitor', 1, 299.99),
        (5, 3, 'Headphones', 1, 129.99)
    ]
    
    cursor.executemany('''
    INSERT OR IGNORE INTO orders (order_id, user_id, product_name, quantity, price)
    VALUES (?, ?, ?, ?, ?)
    ''', orders_data)
    
    conn.commit()
    conn.close()
    print("Database and tables created successfully with sample data!")

# Run this to set up the database
create_database_and_tables()