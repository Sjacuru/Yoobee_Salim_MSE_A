from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

     # Create a quantum circuit with 2 qubits and 2 classical bits
circuit = QuantumCircuit(2, 2)
circuit.h(0)  # Add Hadamard gate to qubit 0
circuit.cx(0, 1)  # Add CNOT gate (control: qubit 0, target: qubit 1)
circuit.measure([0, 1], [0, 1])  # Measure both qubits

     # Simulate the circuit
simulator = AerSimulator()
result = simulator.run(circuit, shots=1000).result()
counts = result.get_counts()
print("Measurement results:", counts)

     # Visualize the circuit
circuit.draw(output='mpl', filename='bell_circuit.png')