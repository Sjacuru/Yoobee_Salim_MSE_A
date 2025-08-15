# 1 - Addition of two complex numbers
def complex_add(z1, z2):
    return z1 + z2

# 2 - Additive inverse (negation) of a complex number
def complex_inverse(z):
    return -z

# 3 - Scalar multiplication of a complex number
def complex_scalar_multiply(scalar, z):
    return scalar * z

# Example usage:
if __name__ == "__main__":
    # Example complex numbers
    z1 = complex(3, 4)   # 3 + 4j
    z2 = complex(1, -2)  # 1 - 2j
    scalar = 2

    print("z1 =", z1)
    print("z2 =", z2)

    # Addition
    print("\nAddition:", complex_add(z1, z2))

    # Inverse
    print("Inverse of z1:", complex_inverse(z1))

    # Scalar multiplication
    print("Scalar multiplication (2 * z1):", complex_scalar_multiply(scalar, z1))
