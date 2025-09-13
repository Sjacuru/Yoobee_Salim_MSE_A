import sqlite3

def create_connection():
    conn = sqlite3.connect("Mydatabase.db")
    return conn

class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    
class OrderService:
    def get_orders(self, order_id):
        conn = sqlite3.connect("orders.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        result = cursor.fetchone()
        conn.close()
        return result