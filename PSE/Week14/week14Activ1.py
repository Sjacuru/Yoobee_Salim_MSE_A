
'''
THe decorator takes a function that takes another function as an 
argument, returning a new function extending its functionality.
'''

def log_decorator(func):
    print('Step 1')
    def wrapper(*args, **kwargs):
        print('Step 2')
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        print('Step 3')
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    print('Step 4')
    return wrapper
    
@log_decorator
def add(a, b):
        print('Step 5')
        return a + b
        
def main():
     
    add(3, 5)

if __name__ == "__main__":
    main()