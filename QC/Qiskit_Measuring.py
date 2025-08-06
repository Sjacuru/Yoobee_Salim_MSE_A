from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator

# Create a simple quantum circuit with 1 qubit
qc = QuantumCircuit(1)
qc.h(0)  # Apply Hadamard gate to put qubit in superposition
qc.measure_all()

# Use AerSimulator as backend
simulator = AerSimulator()

# Transpile the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Run the simulation
result = simulator.run(compiled_circuit).result()

# Get counts (measurement results)
counts = result.get_counts(qc)
print("Measurement results:", counts)