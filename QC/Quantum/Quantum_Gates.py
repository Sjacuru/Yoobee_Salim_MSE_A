from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 1 qubit and 1 classical bit (for measurement)
qc = QuantumCircuit(1, 1)



# Apply an X gate (flips |0⟩ to |1⟩) - 
qc.x(0)

# Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Draw the circuit
print(qc.draw(output='text'))

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts = result.get_counts(qc)

# Plot the results (should always be "1")
plot_histogram(counts)

# Hadamart Gate

qc = QuantumCircuit(1, 1)

# Apply Hadamard gate (creates superposition)
qc.h(0)

# Measure
qc.measure(0, 0)

print(qc.draw(output='text'))

# Simulate (results will be ~50% "0" and ~50% "1")
result = execute(qc, simulator, shots=1000).result()
plot_histogram(result.get_counts(qc))

# Phase flip (S adn T)

qc = QuantumCircuit(1, 1)

# Apply Hadamard to create superposition
qc.h(0)

# Apply S gate (adds a 90° phase to |1⟩)
qc.s(0)

# Apply another Hadamard to interfere the phases
qc.h(0)

# Measure
qc.measure(0, 0)

print(qc.draw(output='text'))

# Simulate (results will now be deterministic due to phase interference)
result = execute(qc, simulator, shots=1000).result()
plot_histogram(result.get_counts(qc))

# Rotation Gates (Rxyz)

import numpy as np

qc = QuantumCircuit(1, 1)

# Rotate around Y-axis by pi/2 (90°)
qc.ry(np.pi/2, 0)

# Measure
qc.measure(0, 0)

print(qc.draw(output='text'))

# Simulate (results will be ~50/50 since ry(pi/2) creates a superposition)
result = execute(qc, simulator, shots=1000).result()
plot_histogram(result.get_counts(qc))

# Entanglement 

qc = QuantumCircuit(2, 2)

# Apply Hadamard to qubit 0
qc.h(0)

# Apply CNOT (control=0, target=1)
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

print(qc.draw(output='text'))

# Simulate (results will be "00" or "11" with 50% probability each)
result = execute(qc, simulator, shots=1000).result()
plot_histogram(result.get_counts(qc))