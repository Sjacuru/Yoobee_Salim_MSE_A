
'''
THe decorator takes a function that takes another function as an 
argument, returning a new function extending its functionality.
'''

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
    
@log_decorator
def add(a, b):
        return a + b
     
add(3, 5)


