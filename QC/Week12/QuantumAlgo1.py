import qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, circuit_drawer
import matplotlib.pyplot as plt

circ = QuantumCircuit(2, 2)     # 2 qubits, 2 classical bits (Activate measurement)
# circ = QuantumCircuit(2)        # 2 qubits, no classical bits (deactivate measurement)
circ.h(0)                       # Hadamard gate on qubit 
circ.cx(0, 1)                   # CNOT gate with qubit 0 as control and qubit 1 as target

# print the bloch sphere
state = Statevector(circ)
print(plot_bloch_multivector(state, reverse_bits=True))

# Print the circuit
# circ.measure([0,1], [0,1]) # measure both qubits into classical bits, remove it if no classical bits are used
circ.draw('mpl')
plt.show()