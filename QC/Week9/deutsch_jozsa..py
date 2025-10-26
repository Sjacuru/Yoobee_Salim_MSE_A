# deutsch_jozsa.py
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def constant_oracle(qc):
    qc.x(1)  # Constant function (always outputs 1)

def balanced_oracle(qc):
    qc.cx(0, 1)  # Balanced function (CNOT: flips output if input is |1⟩)

# Build the circuit
n = 1  # Number of input qubits
qc = QuantumCircuit(n+1, n)

# Initialize output qubit to |1⟩ and apply Hadamard
qc.x(n)
qc.h(n)

# Apply Hadamard to input qubits
for qubit in range(n):
    qc.h(qubit)

# Choose the oracle (uncomment one)
constant_oracle(qc)  # Uncomment for constant function
# balanced_oracle(qc)  # Uncomment for balanced function

# Apply Hadamard to input qubits again
for qubit in range(n):
    qc.h(qubit)

# Measure input qubits
qc.measure(range(n), range(n))

# Draw the circuit (optional)
print("Quantum Circuit:")
print(qc.draw(output='text'))

# Simulate
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts(qc)

# Plot results
print("\nMeasurement Results:", counts)
plot_histogram(counts)
plt.show()