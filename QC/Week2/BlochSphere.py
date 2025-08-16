import qiskit as qk
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt  # Required to display the plot

# Create a quantum circuit with 1 qubit
qc = qk.QuantumCircuit(1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Initialize to |1⟩ by applying X-gate to |0⟩
#qc.x(0)  # X-gate flips |0⟩ to |1⟩

# Get the statevector
statevector = Statevector.from_instruction(qc)

# Plot on Bloch sphere
bloch_sphere = plot_bloch_multivector(statevector)

# Display the plot
plt.show()  # This is crucial to actually see the visualization

#print(statevector)