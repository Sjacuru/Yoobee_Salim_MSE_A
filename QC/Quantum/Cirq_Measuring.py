import cirq
qubit = cirq.GridQubit(0, 0)

# Create a circuit: apply Hadamard gate then measure
circuit = cirq.Circuit(
    cirq.H(qubit),
    cirq.measure(qubit, key='result')
)

# Create a simulator
simulator = cirq.Simulator()

# Run the simulation 1000 times
result = simulator.run(circuit, repetitions=1000)

# Print measurement results
print(result.histogram(key='result'))