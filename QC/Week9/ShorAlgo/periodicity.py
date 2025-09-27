import numpy as np

def periodic_oracle_matrix(num_input_qubits: int):
    """
    Build the oracle matrix U_f for f(x) = x mod 2.
    num_input_qubits = 2 -> 2 input qubits (4 inputs)
    num_input_qubits = 3 -> 3 input qubits (8 inputs)
    Returns a 2^(n+1) x 2^(n+1) matrix (since we add 1 output qubit).
    """
    num_inputs = 2 ** num_input_qubits
    num_qubits_total = num_input_qubits + 1  # add 1 output qubit
    dim = 2 ** num_qubits_total

    # Start with identity (we'll permute rows)
    U = np.zeros((dim, dim), dtype=int)

    for x in range(num_inputs):
        fx = x % 2  # periodic function f(x) = x mod 2

        for y in [0, 1]:  # output qubit state
            in_index = (x << 1) | y   # binary encoding
            out_y = y ^ fx            # apply y XOR f(x)
            out_index = (x << 1) | out_y
            U[out_index, in_index] = 1

    return U


# Example usage:
U2 = periodic_oracle_matrix(2)  # 2 input qubits
U3 = periodic_oracle_matrix(3)  # 3 input qubits

print("Oracle with 2 input qubits (dimension = {}):".format(U2.shape))
print(U2)

print("\nOracle with 3 input qubits (dimension = {}):".format(U3.shape))
print(U3)
