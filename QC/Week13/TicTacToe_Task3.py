from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
# Data handling and communication
import json  # For working with JSON (JavaScript Object Notation) data
import requests  # For making HTTP requests to the Quokka
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning


circ = QuantumCircuit(2)  
circ.h(0)                       
circ.cx(0, 1)                    

circ.draw('mpl')

state = Statevector(circ)
plot_bloch_multivector(state, reverse_bits=True)


program = """  
OPENQASM 2.0;
"""
# Number of qubits
program += """
qreg q[2];
"""
# Inicializing classical registers
program += """
creg c[2];
"""
# Quantum circuits to create a Bell State
program += """
h q[0];
cx q[0], q[1];
"""
# Measurement
program += """
measure q[0] -> c[0];
measure q[1] -> c[1];
"""


# Suppressing warnings (optional)
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable warnings about insecure requests


# default Quokka address (change if you have your own!):
my_quokka = 'quokka1'

# the complete addresss
request_http = 'http://{}.quokkacomputing.com/qsim/qasm'.format(my_quokka)

# create dictionary
data = {
    'script': program,
    'count': 10
}

# send the request
result = requests.post(request_http, json=data, verify=False)

# load the object into a Python dictionary
json_obj = json.loads(result.content)

# print the keys and entries
print(json_obj)


def make_move(self, cell):
    qbit = int(cell)
    if self.function == 'Not':
        # add an $x$ gate
        self.qc.x(qbit)
        self.tab[int(cell)]['player'] += 'N - '
    elif self.function == 'O':
        # add a rotation toward |0>
        self.qc.ry(-math.pi/2, qbit)
        self.tab[int(cell)]['player'] += "O - "
    elif self.function == 'X':
        # add a rotation toward |1>
        self.qc.ry(math.pi/2, qbit)
        self.tab[int(cell)]['player'] += "X - "
    elif self.function == 'SWAP' and self.target != cell:
        target_qbit = int(self.target)
        if self.target == cell:
            self.target = -1
        else:
            # add a swap gate
            self.qc.swap(qbit, target_qbit)
            self.tab[int(cell)]['player'] += "S - "
            self.tab[int(self.target)]['player'] += "S - "