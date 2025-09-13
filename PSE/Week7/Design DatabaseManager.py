import sqlite3
import time

class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect('Mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    
class OrderService:
    def get_orders(self, order_id):
        conn = sqlite3.connect("Mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    
        
def main():
    userService = UserService()
    orderService = OrderService()
    
    start_time = time.perf_counter()
    user = userService.get_user(1)
    print("User Details:", user)
    
    orders = orderService.get_orders(1)
    print("User Orders:", orders)

    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.8f} seconds")

if __name__ == '__main__':
    main()


