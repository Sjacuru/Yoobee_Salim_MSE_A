import qiskit as qk
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
# Create a quantum circuit with two qubits and two classical bits
qc = qk.QuantumCircuit(2, 2)

# Apply Hadamard gate to both qubits
qc.h(0)
qc.h(1)

# Measure both qubits
qc.measure(0, 0)
qc.measure(1, 1)

# Choose the qasm_simulator backend
simulator = AerSimulator(method='statevector')

# Simulate the circuit
job = simulator.run(qc, shots=1024)

# Get the result
result = job.result()

# Print the counts
print(result.get_counts(qc))

# Visualize the circuit
print(qc)
qc.draw(output='mpl').show()

# Visualize the measurement outcomes
plot_histogram(result.get_counts(qc))