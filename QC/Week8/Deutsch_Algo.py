import cirq
import numpy as np

# Function to create an oracle gate from a given unitary matrix
def create_oracle_gate(oracle_matrix):
    return cirq.MatrixGate(oracle_matrix, num_qubits=2)

# Function to prompt the user to input a 4x4 unitary matrix
def input_unitary_matrix():
    
    #print("Enter the 64 comma-separated values for the 8x8 unitary matrix:")
    print("Enter the 16 comma-separated values for the 4x4 unitary matrix (row-major order):")
    #matrix_values = input().strip().split(',')
    #oracle_matrix = np.array([[float(matrix_values[i]) for i in range(8)],
    #                          [float(matrix_values[i]) for i in range(8, 16)],
    #                          [float(matrix_values[i]) for i in range(16, 24)],
    #                          [float(matrix_values[i]) for i in range(24, 32)],
    #                          [float(matrix_values[i]) for i in range(32, 40)],
    #                          [float(matrix_values[i]) for i in range(40, 48)],
    #                          [float(matrix_values[i]) for i in range(48, 56)],
    #                          [float(matrix_values[i]) for i in range(56, 64)]])
    #return oracle_matrix
    #input_str = input().strip()
    input_str = "1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1" # Constant oracle (Identity)
    matrix_values = [float(val) for val in input_str.split(',')]

    if len(matrix_values) != 16:
        raise ValueError(f"Expected 16 values for a 4x4 matrix, but got {len(matrix_values)}.")

    oracle_matrix = np.array(matrix_values).reshape((4, 4))
    return oracle_matrix

#def determine_function_type(circuit_result):
    # Get the measurement outcomes of the initial two qubits
#    measurement_outcomes = [circuit_result.measurements[f'result_{i}'][0][0] for i in range(2)]

    # Determine the type of function based on the measurement outcomes
#    if all(outcome == 0 for outcome in measurement_outcomes):
#        return "constant"
#    else:
#        return "balanced"

def determine_function_type(measurement_outcomes_list):
    # Check all measurements - if ALL results are [0, 0], the function is constant
    if all(outcomes == [0, 0] for outcomes in measurement_outcomes_list):
        return "constant"
    else:
        return "balanced"



# Define Deutsch's algorithm
def deutsch_algorithm(oracle_gate):
    # Define qubits
    qubits = cirq.LineQubit.range(2)

    # Create a quantum circuit
    circuit = cirq.Circuit()

   
# Apply X gate (NOT gate) on the third qubit
#    circuit.append(cirq.X(qubits[-1]))

    # Initialize the second qubit to |1⟩ for phase kickback
    circuit.append(cirq.X(qubits[1]))


# Apply Hadamard gate to all qubits
    circuit.append([cirq.H(q) for q in qubits])

# Apply the matrix gate on all inputs
    circuit.append(oracle_gate(*qubits))

# Apply Hadamard gate to all outputs except the last qubit
#    for qubit in qubits[:-1]:
#        circuit.append(cirq.H(qubit))

    circuit.append(cirq.H(qubits[0]))


   # Measure the initial two qubits
   # circuit.append([cirq.measure(q, key=f'result_{i}') for i, q in enumerate(qubits[:2])])

    # Measure both qubits
    circuit.append([cirq.measure(q, key=f'result_{i}') for i, q in enumerate(qubits)])

    return circuit

print("="*60)
print("2-Qubit Deutsch Algorithm")
print("="*60)
print("The oracle must be a 4x4 unitary matrix.")
print("Enter 16 values, row by row, separated by commas.")
# Prompt the user to input the 4x4 unitary matrix

oracle_matrix = input_unitary_matrix()

# Create the oracle gate from the user-defined unitary matrix
oracle_gate = create_oracle_gate(oracle_matrix)

# Run Deutsch's algorithm with the user-defined oracle gate
circuit = deutsch_algorithm(oracle_gate)

# Simulate the circuit 5 times and collect results
simulator = cirq.Simulator()
results = simulator.run(circuit, repetitions=10)

measurement_outcomes_list = []

for _ in range(10):
    result = simulator.run(circuit)
    outcomes = [results.measurements[f'result_{j}'][i] for j in range(2)]
    measurement_outcomes = [result.measurements[f'result_{i}'][0][0] for i in range(2)]
    measurement_outcomes_list.append(measurement_outcomes)
    
# Print all measurement outcomes
#print("Measurement outcomes:", measurement_outcomes_list)
print("\nMeasurement outcomes (result_0, result_1):")
for i, outcomes in enumerate(measurement_outcomes_list):
    print(f"Run {i+1}: {outcomes}")  

# Determine the type of function based on the measurement outcomes
#function_type = determine_function_type(result)
function_type = determine_function_type(measurement_outcomes_list)
print("Function type:", function_type)

# Print the circuit
print("\nCircuit:")
print(circuit)

