# Deutsch2_aer.py
# Deutsch-Jozsa (1-bit) — execução local com AerSimulator
# Salim — Yoobee / MSE
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from enum import Enum

# --- CONFIGURAÇÃO ---
shots = 1024  # aumente para estatísticas melhores no simulador

# --- FUNÇÕES DO ALGORITMO DE DEUTSCH-JOZSA ---
class SimpleBinary(Enum):
    ONE = 1
    SAME_AS = 2
    OPPOSITE_OF = 3

def get_oracle(circ, function):
    """
    Aplica o oráculo ao circuito circ de 2 qubits (q0 = input, q1 = work).
    Para ZERO (function == 0) o oráculo não faz nada.
    """
    if function == SimpleBinary.ONE:      # Constante 1
        circ.x(1)
    elif function == SimpleBinary.SAME_AS:   # Balanceada: f(x) = x
        circ.cx(0, 1)
    elif function == SimpleBinary.OPPOSITE_OF: # Balanceada: f(x) = NOT x
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

# Preparação do estado de trabalho e superposição
circ.x(1)      # coloca o qubit de trabalho em |1>
circ.h(0)
circ.h(1)
circ.barrier()

if function == 0:
    print("Função ZERO (Constant) selecionada.")
else:
    print(f"Função {function.name} selecionada.")

# Aplica o oráculo (pode ser "nenhuma operação" para ZERO)
circ = get_oracle(circ, function)
circ.barrier()

# Finaliza: H no primeiro qubit e mede
circ.h(0)
circ.measure(0, 0)

print("\nCircuito construído:")
print(circ)

# --- EXECUÇÃO NO SIMULADOR LOCAL (Aer) ---
sim = AerSimulator()
compiled = transpile(circ, sim)

print("\nExecutando no AerSimulator (local)...")
job = sim.run(compiled, shots=shots)
result = job.result()

print("\n--- Resultado (simulador Aer) ---")
counts = result.get_counts()
print(f"Contagens: {counts}")

# Interpretação dos resultados
number_of_0s = counts.get('0', 0)
number_of_1s = counts.get('1', 0)

if number_of_0s == shots:
    print('Resultado Deutsch-Jozsa: Constant')
elif number_of_1s == shots:
    print('Resultado Deutsch-Jozsa: Balanced')
else:
    p0 = number_of_0s / shots * 100
    p1 = number_of_1s / shots * 100
    print("Os resultados não são 100% conclusivos (porcentagens abaixo).")
    print(f"Probabilidades aproximadas: 0 -> {p0:.2f}%, 1 -> {p1:.2f}%")

# (Opcional) Mostra as probabilidades em formato legível
total = sum(counts.values()) if counts else shots
print("\nProbabilidades detalhadas:")
for bitstring, cnt in counts.items():
    print(f"  {bitstring} : {cnt} / {total} = {cnt/total*100:.2f}%")
