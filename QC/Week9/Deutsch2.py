from qiskit import QuantumCircuit
from enum import Enum
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from qiskit.providers.exceptions import QiskitBackendNotFoundError

# --- CONFIGURAÇÃO DE SERVIÇO IBM QISKIT RUNTIME ---
# SEU CRN: Única fonte de verdade para a sua instância na IBM Cloud.
CRN = 'crn:v1:bluemix:public:quantum-computing:us-east:a/c8ad836f08cf48edaa62e5faeef955f8:b6216418-815a-433b-a97a-c8d45f14e4bf::'

# BACKEND ALOCADO: Usando o QPU que sua conta alocada permite.
BACKEND_NAME = 'ibm_brisbane'
shots = 1

# 1. Inicializa o service com seu CRN.
service = QiskitRuntimeService(instance=CRN)

# --- FUNÇÕES DO ALGORITMO DE DEUTSCH-JOZSA ---
class SimpleBinary(Enum):
    ONE = 1
    SAME_AS = 2
    OPPOSITE_OF = 3

def get_oracle(circ, function):
    # function == None/0 -> ZERO (faz nada)
    if function == SimpleBinary.ONE:      # Constante 1
        circ.x(1)
    elif function == SimpleBinary.SAME_AS:   # Balanceada
        circ.cx(0, 1)
    elif function == SimpleBinary.OPPOSITE_OF: # Balanceada
        circ.cx(0, 1)
        circ.x(1)
    return circ

def get_function():
    print('Which function? (0/1/2/3)')
    print(' 0: ZERO (Constant - default)')
    print(' 1: ONE (Constant)')
    print(' 2: SAME_AS (Balanced)')
    print(' 3: OPPOSITE_OF (Balanced)')

    try:
        value = int(input('> '))
        if 0 <= value <= 3:
            return SimpleBinary(value) if value > 0 else 0
    except ValueError:
        return 0
    return 0

# --- CONSTRUÇÃO DO CIRCUITO ---
circ = QuantumCircuit(2, 1)
function = get_function()

# Preparação padrão do Deutsch-Jozsa (para 1-bit f)
# Estado inicial |1> no segundo qubit para flip phase
circ.x(1)
# Aplica H nos dois qubits
circ.h(0)
circ.h(1)
circ.barrier()

# Aplica o Oráculo (para ZERO o oráculo faz nada)
if function == 0:
    print("Função ZERO (Constant) selecionada.")
else:
    print(f"Função {function.name} selecionada.")

circ = get_oracle(circ, function)
circ.barrier()

# Aplica H no primeiro qubit e faz a medição
circ.h(0)
circ.measure(0, 0)

print(circ)

# --- EXECUÇÃO NA IBM QUANTUM RUNTIME (Estrutura V2 final) ---
print("\n--- Execução na IBM Quantum Runtime ---")

# --- PASSO CRUCIAL: OBTER O OBJETO BACKEND ---
try:
    backend_obj = service.backend(BACKEND_NAME)
    print(f"Backend '{BACKEND_NAME}' carregado com sucesso.")
except QiskitBackendNotFoundError as e:
    print(f"ERRO: O backend '{BACKEND_NAME}' não foi encontrado. Motivo: {e}")
    exit(1)

# Use Session com o service e backend; crie o Sampler usando a session
with Session(backend=backend_obj) as session:
    print(f"Enviando job para {backend_obj.name}...")

    # Inicializa o Sampler usando a session atual
    sampler = Sampler(session=session)

    # Execute o job
    job = sampler.run(
        circuits=[circ],
        shots=shots
    )

    # Obtenha o resultado
    job_id = job.job_id()
    print(f"Job ID: {job_id}")
    print("Aguardando resultado...")

    # Este é um QPU real, o resultado pode levar tempo.
    result = job.result()

# --- PROCESSAMENTO DOS RESULTADOS ---
print(f"Resultado recebido do Job ID: {job_id}")

quasi_dist = result.quasi_dists[0]
# transforma quasi-dists em counts inteiros (aproximando pelo número de shots)
counts = {str(k): int(v * shots) for k, v in quasi_dist.items()}

print(f"\nFunção escolhida: {function.name if function != 0 else 'ZERO'}")
print(f"Contagem de resultados: {counts}")

number_of_0s = counts.get('0', 0)
number_of_1s = counts.get('1', 0)

# Lógica de decisão de Deutsch-Jozsa
if number_of_0s == shots:
    print('Resultado Deutsch-Jozsa: Constant')
elif number_of_1s == shots:
    print('Resultado Deutsch-Jozsa: Balanced')
else:
    print("Os resultados não são conclusivos. (Verifique 'shots' ou 'function')")
