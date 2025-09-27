from qiskit import QuantumCircuit
from enum import Enum
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session 


CRN = 'crn:v1:bluemix:public:quantum-computing:us-east:a/c8ad836f08cf48edaa62e5faeef955f8:b6216418-815a-433b-a97a-c8d45f14e4bf::'
service = QiskitRuntimeService(instance=CRN) 

device = service.least_busy()


class SimpleBinary(Enum):    
    ONE = 1
    SAME_AS = 2
    OPPOSITE_OF = 3
def get_oracle(circ, function):    
# if function == SimpleBinary.ZERO:
# Do nothing
    if function == SimpleBinary.ONE:
        circ.x(1)
    elif function == SimpleBinary.SAME_AS:
        circ.cx(0, 1)
    elif function == SimpleBinary.OPPOSITE_OF:
        circ.cx(0, 1)
        circ.x(1)
    return circ

def get_function():    
    print('Which function? (0/1/2/3)')
    print(' 0: ZERO')
    print(' 1: ONE')
    print(' 2: SAME_AS')
    print(' 3: OPPOSITE_OF')
    value = input('> ')
    return SimpleBinary(int(value))

circ = QuantumCircuit(2, 1)
function = get_function()
circ.x(1)
circ.h(0)
circ.h(1)
circ.barrier()
circ = get_oracle(circ, function)
circ.barrier()
circ.h(0)
circ.measure(0, 0)
print(circ)


#It runs Deutsch’s algorithm on a simulator, but needs API Token to run on IBM Quantum Experience.:

SIMULATOR_NAME = 'simulator_statevector' 

with Session(service=service, backend=SIMULATOR_NAME) as session:
    
    # 3. Inicialize o Sampler DENTRO da Session (sem argumentos!)
    sampler = Sampler() 

    print(f"Enviando job para {SIMULATOR_NAME}...")

    # 4. Execute o job. O Sampler usa o backend e o serviço da Session.
    job = sampler.run(
        circuits=[circ], 
        shots=1
    )

    # 5. Obtenha e imprima o resultado
    job_id = job.job_id()
    print(f"Job ID: {job_id}")
    print("Aguardando resultado...")

    result = job.result()

shots = 1
print(job.job_id())
result = job.result()
quasi_dist = result.quasi_dists[0]
counts = {str(k): int(v * 1) for k, v in quasi_dist.items()}
print(function)
print(counts)
number_of_0s = counts.get('0')
number_of_1s = counts.get('1')
if number_of_0s is not None and number_of_0s == shots:
    print('Constant')
elif number_of_1s is not None and number_of_1s == shots:
    print('Balanced')
else:
    print("Results aren't conclusive")