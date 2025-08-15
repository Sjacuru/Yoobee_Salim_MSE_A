# Complex Number Operations

# Step 1: Define two complex numbers
z1 = complex(4, 3)   # 4 + 3j
z2 = complex(2, -1)  # 2 - 1j

print("z1 =", z1)
print("z2 =", z2)

# Step 2: Perform operations
print("\n--- Operations ---")
print("Addition:     ", z1 + z2)
print("Subtraction:  ", z1 - z2)
print("Multiplication:", z1 * z2)
print("Division:     ", z1 / z2)

# Step 3: Get user input for a complex number
print("\n--- User Input ---")
user_input = input("Enter a complex number (e.g., 3+4j): ")
user_complex = complex(user_input)

# Step 4: Show modulus and conjugate
print("Your number:  ", user_complex)
print("Modulus:      ", abs(user_complex))
print("Conjugate:    ", user_complex.conjugate())
