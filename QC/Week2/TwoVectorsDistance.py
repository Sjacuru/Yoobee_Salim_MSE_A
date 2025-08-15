import math

def complex_distance(z1, z2):
    """
    Calculate the Euclidean distance between two complex numbers z1 and z2.

    Parameters:
        z1 (complex): First complex number (e.g., 1+2j).
        z2 (complex): Second complex number (e.g., 3+4j).

    Returns:
        float: The distance between z1 and z2.
    """
    return abs(z1 - z2)  # Built-in `abs` computes the magnitude of the difference

# Example usage
z1 = 1 + 2j
z2 = 3 + 4j
print(complex_distance(z1, z2))  # Output: 2.8284271247461903 (√8 ≈ 2.828)