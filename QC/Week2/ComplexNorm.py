import math

def complex_norm(z):
    """
    Calculate the norm (magnitude) of a complex number z.

    Parameters:
        z (complex or float): A complex number (e.g., 3+4j) or real number.

    Returns:
        float: The norm (magnitude) of z.
    """
    return math.sqrt(z.real**2 + z.imag**2)

# Example usage
z = 3 + 4j
print(complex_norm(z))  # Output: 5.0 (since √(3² + 4²) = 5)