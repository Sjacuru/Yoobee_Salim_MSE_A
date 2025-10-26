import unittest
import doctest

def add(a, b):
    '''
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0  # Corrected from the original code
    '''
    return a + b    

def subtract(a, b):  
    '''
    >>> subtract(10, 5)
    5
    >>> subtract(0, 0)
    0
    >>> subtract(-1, 1)
    -2
    '''
    return a - b    

def multiply(a, b): 
    '''
    >>> multiply(3, 4)
    12
    >>> multiply(0, 5)
    0
    >>> multiply(-2, 3)
    -6
    '''
    return a * b        

def divide(a, b):   
    '''
    >>> divide(10, 2)
    5.0
    >>> divide(10, 3)
    3.3333333333333335  # Note: Floating-point results may vary slightly
    >>> divide(5, 1)
    5.0
    '''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b    

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 1)  #  fail

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 1)  # fail

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 11)  # 
        self.assertEqual(multiply(3, 4), 12)  # fail

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), 0)  # fail

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    # Run doctests first
    import doctest
    doctest.testmod()
    
    # Then run unit tests
    unittest.main()