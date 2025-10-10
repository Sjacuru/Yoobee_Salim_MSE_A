import unittest

def add(a, b):
    return a + b    

def subtract(a, b):  
    return a - b    

def multiply(a, b): 
    return a * b        

def divide(a, b):   
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b    

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 1)  # error

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 1)  # error

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 11)  # error
        self.assertEqual(multiply(3, 4), 12)  # error

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), 0)  # error

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()