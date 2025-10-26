# oracle_builder.py
import numpy as np

# Optional Qiskit parts (only used if qiskit is installed)
try:
    from qiskit import QuantumCircuit, transpile
    from qiskit.quantum_info import Operator, Statevector
    from qiskit.providers.aer import AerSimulator
    QISKIT_AVAILABLE = True
except Exception:
    QISKIT_AVAILABLE = False

def bitstr_to_int(b):
    return int(b, 2)

def int_to_bitstr(i, width):
    return format(i, '0{}b'.format(width))

def build_oracle_matrix(mapping: dict):
    """
    Build U_f matrix for a mapping: keys are input bitstrings (length n),
    values are output bitstrings (length m). The oracle performs:
      |x>|y> -> |x>|y XOR f(x)>
    Returns: numpy array of shape (2^(n+m), 2^(n+m))
    """
    # infer sizes
    input_bits = len(next(iter(mapping.keys())))
    output_bits = len(next(iter(mapping.values())))

    # sanity checks
    for k, v in mapping.items():
        assert len(k) == input_bits, "All keys must have same length"
        assert len(v) == output_bits, "All values must have same length"

    N_inputs = 2 ** input_bits
    dim = 2 ** (input_bits + output_bits)
    U = np.zeros((dim, dim), dtype=int)

    # For each x in domain and each y in {0..2^m-1}
    for x_bs, f_bs in mapping.items():
        x = bitstr_to_int(x_bs)
        fx = bitstr_to_int(f_bs)
        for y in range(2 ** output_bits):
            in_index = (x << output_bits) | y
            out_y = y ^ fx  # XOR at bitlevel
            out_index = (x << output_bits) | out_y
            U[out_index, in_index] = 1

    return U

def build_qiskit_oracle_circuit(U: np.ndarray, n_input_qubits: int, n_output_qubits: int):
    """
    Build a Qiskit QuantumCircuit implementing the oracle U (unitary matrix).
    Requires qiskit installed. Returns QuantumCircuit.
    """
    if not QISKIT_AVAILABLE:
        raise RuntimeError("Qiskit not available in this Python environment.")

    total_qubits = n_input_qubits + n_output_qubits
    qc = QuantumCircuit(total_qubits)
    op = Operator(U)
    qc.append(op, range(total_qubits))
    return qc

def classical_period_from_mapping(mapping: dict):
    """
    Compute period r: smallest positive r such that f(x) == f((x+r) mod N) for all x.
    Returns r (int) or None if no period found.
    """
    input_bits = len(next(iter(mapping.keys())))
    N = 2 ** input_bits

    # create list f(x) in canonical order 0..N-1 (original values as strings)
    f_list = [mapping[int_to_bitstr(x, input_bits)] for x in range(N)]

    # check periods r = 1..N
    for r in range(1, N+1):
        ok = True
        for x in range(N):
            if f_list[x] != f_list[(x + r) % N]:
                ok = False
                break
        if ok:
            return r
    return None

def simulate_oracle_on_superposition(U: np.ndarray, n_input_qubits: int, n_output_qubits: int, shots=1024):
    """
    Try to simulate the oracle applied to |+>^n_input |0>^m_output.
    If Qiskit Aer available, run with simulator; otherwise use numpy Statevector.
    Prints resulting state amplitudes / probabilities for reduced input register.
    """
    total_qubits = n_input_qubits + n_output_qubits
    dim = 2 ** total_qubits

    # build initial state |+>^n |0>^m
    # input superposition statevector for n input qubits
    psi_in = (1 / np.sqrt(2 ** n_input_qubits)) * np.ones(2 ** n_input_qubits, dtype=complex)
    psi_out = np.zeros(2 ** n_output_qubits, dtype=complex)
    psi_out[0] = 1.0
    # full tensor product
    psi0 = np.kron(psi_in, psi_out)  # shape (dim,)

    # apply U
    psi_final = U.dot(psi0)

    # compute reduced density (or probabilities) of input register by summing probs over output states
    probs = np.zeros(2 ** n_input_qubits)
    for x in range(2 ** n_input_qubits):
        # states with same x are indices (x << m) + y
        block = psi_final[(x << n_output_qubits) : ((x+1) << n_output_qubits)]
        probs[x] = np.sum(np.abs(block) ** 2)

    print("Probabilities on the input register after oracle (classical sim):")
    for x, p in enumerate(probs):
        print(f"  {int_to_bitstr(x, n_input_qubits)} : {p:.6f}")

    # If qiskit available, show circuit (optional)
    if QISKIT_AVAILABLE:
        print("\nQiskit is available. Building circuit and showing statevector (transpilation skipped).")
        qc = build_qiskit_oracle_circuit(U, n_input_qubits, n_output_qubits)
        sv = Statevector.from_label('+'*n_input_qubits + '0'*n_output_qubits)
        sv2 = sv.evolve(Operator(U))
        # compute reduced probs same way
        probs_q = np.zeros(2 ** n_input_qubits)
        amp = sv2.data
        for x in range(2 ** n_input_qubits):
            block = amp[(x << n_output_qubits) : ((x+1) << n_output_qubits)]
            probs_q[x] = np.sum(np.abs(block) ** 2)
        print("Probabilities computed via Qiskit Statevector (should match):")
        for x, p in enumerate(probs_q):
            print(f"  {int_to_bitstr(x, n_input_qubits)} : {p:.6f}")

# ---------------------------
# Example: your mapping
# ---------------------------
if __name__ == "__main__":
    # Your mapping: inputs (2 bits) -> outputs (2 bits)
    mapping_2q = {
        "00": "00",
        "01": "11",
        "10": "00",
        "11": "11",
    }

    U = build_oracle_matrix(mapping_2q)
    print("Oracle matrix U (rows = outputs, cols = inputs) shape:", U.shape)
    np.set_printoptions(linewidth=200, threshold=200)
    print(U)

    r = classical_period_from_mapping(mapping_2q)
    print("\nClassical detected period r =", r)

    # Simulate oracle acting on input |+,+> and output |00>
    simulate_oracle_on_superposition(U, n_input_qubits=2, n_output_qubits=2)
