from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
# Data handling and communication
import json  # For working with JSON (JavaScript Object Notation) data
import requests  # For making HTTP requests to the Quokka
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning



def quantum_search_assistant():
    qc = QuantumCircuit(3, 2)
    qc.h(0)  
    qc.x(1)  

    qc.cx(0, 2)    # Controlled-NOT gate: qubit 0 controls qubit 2
    qc.h(2)        # Hadamard gate on qubit 2
    qc.x(0)        # Flip qubit 0
    qc.cx(0, 2)    # Another Controlled-NOT, qubit 0 controls qubit 2
    qc.x(0)        # Flip qubit 0 back

    qc.measure(0, 0)  # Qubit 0 stored in classical bit 0
    qc.measure(2, 1)  # qubit 2 stored in classical bit 1

    return qc

# === EXECUTE AND ANALYZE ===
print("=== BUILDING THE QUANTUM SEARCH ASSISTANT ===")
qc = quantum_search_assistant()
print("Quantum Circuit Diagram:")
print(qc.draw())

print("\n=== HOW TO READ THE CIRCUIT ===")
print("H = Hadamard gate (creates superposition)")
print("X = NOT gate (flips 0↔1)")
print("CX = Controlled-NOT (entanglement gate)")
print("M = Measurement (quantum → classical)")
print("q0, q1, q2 = Quantum bits (work in superposition)")
print("c0, c1 = Classical bits (store final results)")


# Run the quantum circuit
print("\n=== RUNNING QUANTUM SEARCH ===")
simulator = AerSimulator()
result = simulator.run(qc, shots=20)  # Run 20 times
counts = result.result().get_counts()

print("\n=== QUANTUM SEARCH SUGGESTIONS ===")
print("The quantum computer analyzed all possibilities and suggests:")
print("Format: [Section A/B] [Section C/D] → Which areas to search")

for suggestion, count in counts.items():
    sections = []
    # First bit (c0) decides between section A or B
    if suggestion[0] == '0':
        sections.append("A")
    else:
        sections.append("B")

    # Second bit (c1) decides between section C or D
    if suggestion[1] == '0':
        sections.append("C")
    else:
        sections.append("D")

    print(f"  {suggestion} → Search in sections: {sections} ({count} votes)")

print("\n=== REAL-WORLD EXAMPLE ===")
print("Imagine searching for a lost file in 4 folders:")
print("Folder A: Work documents")
print("Folder B: Personal files")
print("Folder C: Recent downloads")
print("Folder D: Backup files")
print("\nQuantum says: 'Based on quantum patterns, search in B and D first!'")
print("This saves you from searching A and C unnecessarily.")

print("\"\"\"")
print("=== ASSESSMENT EXPLANATION ===")
print("This quantum search assistant demonstrates three key principles:")
print("")
print("1. QUANTUM PARALLELISM: The Hadamard gates allow the quantum")
print("   computer to consider all possible search areas simultaneously")
print("   rather than checking them one by one.")
print("")
print("2. QUANTUM ENTANGLEMENT: The CNOT gates create correlations")
print("   between qubits, allowing the system to find hidden patterns")
print("   that classical computers might miss.")
print("")
print("3. HYBRID QUANTUM-CLASSICAL COMPUTING: The quantum circuit")
print("   doesn't do the entire search - it identifies promising areas")
print("   and lets the classical computer handle the detailed searching.")
print("   This is how real quantum algorithms work today!")
print("\"\"\"")


program = """
OPENQASM 2.0;
"""
program += """
qreg q[3];
creg c[2];
"""
program += """
h q[0];
x q[1];
"""
program += """
cx q[0], q[2];
h q[2];
x q[0];
cx q[0], q[2];
x q[0];
"""
program += """
measure q[0] -> c[0];
measure q[2] -> c[1];
"""
print(program)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable warnings about insecure requests
# default Quokka address (change if you have your own!):
my_quokka = 'quokka2'
# the complete addresss
request_http = 'http://{}.quokkacomputing.com/qsim/qasm'.format(my_quokka)

# create dictionary
data = {
    'script': program,
    'count': 100
}

# send the request
result = requests.post(request_http, json=data, verify=False)
# load the object into a Python dictionary
json_obj = json.loads(result.content)
# print the keys and entries
print(json_obj)





import matplotlib.pyplot as plt, time

costs, times = [], []
start_time = time.time()

def spsa_with_logging(func, x0, a=1, c=0.5, alpha=0.602, gamma=0.101, maxiter=200):   # copy your spsa, inside loop:
    fx = func(x)
    costs.append(fx)
    times.append(time.time() - start_time)

# run it, then:
plt.figure(figsize=(12,4))
plt.subplot(1,2,1); plt.plot(costs); plt.title('Iteration vs Loss'); plt.xlabel('Iteration'); plt.ylabel('Loss')
plt.subplot(1,2,2); plt.plot(times, costs); plt.title('Time vs Loss'); plt.xlabel('Time (s)'); plt.ylabel('Loss')
plt.tight_layout(); plt.show()