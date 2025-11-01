import time

def timer(func):

    def wrapper(*args, **kwargs):
        
        start_time = time.time()
        print(f"Starting calculation for: {func.__name__}") # name of the original function(add in this case)
        
        result = func(*args, **kwargs) 
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"Finished. Result: {result}")
        print(f"Function '{func.__name__}' took {duration:.4f} seconds.")

        return result
    
    # 'wrapper' function which replaces the original 'add' function.
    return wrapper 

@timer 
def add(a, b):

    print(f"  ...Adding {a} and {b} (simulating a delay)...")
    time.sleep(0.5) 
    return a + b
    
def main():
    print("--- Calling the decorated 'add' function ---")
    
    # This callexecutes the 'wrapper' function inside the 'timer' decorator.
    final_sum = add(3, 5) 
    
    print(f"\nMain function received the sum: {final_sum}")

if __name__ == "__main__":
    main()