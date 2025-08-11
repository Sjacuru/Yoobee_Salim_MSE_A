# bloch_gates.py
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers 3D projection

# Pauli matrices (used to compute Bloch vector)
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

# Gate matrices
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
S = np.array([[1, 0], [0, 1j]], dtype=complex)
T = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]], dtype=complex)
Rx90 = np.array([[np.cos(np.pi/4), -1j*np.sin(np.pi/4)],
                 [-1j*np.sin(np.pi/4), np.cos(np.pi/4)]], dtype=complex)
Ry90 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                 [np.sin(np.pi/4), np.cos(np.pi/4)]], dtype=complex)
Rz90 = np.array([[np.exp(-1j*np.pi/4), 0],
                 [0, np.exp(1j*np.pi/4)]], dtype=complex)

# Table rows (copy-paste friendly descriptions)
table_rows = [
    ("Pauli-X (X)", "[[0, 1], [1, 0]]", "Flips |0> ↔ |1>", "180° rotation around X-axis"),
    ("Pauli-Y (Y)", "[[0, -i], [i, 0]]", "Flips with phase change", "180° rotation around Y-axis"),
    ("Pauli-Z (Z)", "[[1, 0], [0, -1]]", "Phase flip of |1>", "180° rotation around Z-axis"),
    ("Hadamard (H)", "(1/√2) * [[1, 1], [1, -1]]", "Creates/undoes superposition", "Rotation between Z and X basis"),
    ("Phase (S)", "[[1, 0], [0, i]]", "Phase shift π/2 on |1>", "90° rotation around Z-axis"),
    ("T (π/8)", "[[1, 0], [0, e^(iπ/4)]]", "Phase shift π/4 on |1>", "45° rotation around Z-axis"),
    ("Rx(θ)", "[[cos(θ/2), -i sin(θ/2)], [-i sin(θ/2), cos(θ/2)]]", "Rotation by θ around X-axis", "Continuous rotation around X-axis"),
    ("Ry(θ)", "[[cos(θ/2), -sin(θ/2)], [sin(θ/2), cos(θ/2)]]", "Rotation by θ around Y-axis", "Continuous rotation around Y-axis"),
    ("Rz(θ)", "[[e^(-iθ/2), 0], [0, e^(iθ/2)]]", "Rotation by θ around Z-axis", "Continuous rotation around Z-axis"),
    ("CNOT", "4x4 matrix", "Flips target if control=|1>", "Entangles qubits"),
    ("CZ", "4x4 matrix", "Phase flip if control=|1>", "Entangles qubits"),
    ("SWAP", "4x4 matrix", "Swaps two qubits", "Exchanges positions on Bloch spheres")
]

def bloch_vector(state):
    """Return Bloch vector [rx, ry, rz] for a pure state vector."""
    state = state / np.linalg.norm(state)
    rho = np.outer(state, np.conjugate(state))
    rx = np.real(np.trace(rho @ sigma_x))
    ry = np.real(np.trace(rho @ sigma_y))
    rz = np.real(np.trace(rho @ sigma_z))
    return np.array([rx, ry, rz])

def plot_bloch_on_ax(ax, r, title=None):
    # wireframe sphere
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_wireframe(x, y, z, linewidth=0.4, alpha=0.6)
    # axes helpers
    ax.plot([0,1],[0,0],[0,0], color='r')
    ax.plot([0,0],[0,1],[0,0], color='g')
    ax.plot([0,0],[0,0],[0,1], color='b')
    ax.text(1.05,0,0,'X'); ax.text(0,1.05,0,'Y'); ax.text(0,0,1.05,'Z')
    # initial |0> at top
    ax.scatter([0],[0],[1], s=30)
    ax.text(0,0,1.06,"|0>")
    # Bloch vector arrow
    ax.quiver(0,0,0, r[0], r[1], r[2], length=1.0, normalize=True)
    ax.set_xlim([-1,1]); ax.set_ylim([-1,1]); ax.set_zlim([-1,1])
    ax.set_box_aspect([1,1,1])
    if title:
        ax.set_title(title, fontsize=10)

def main():
    outdir = "bloch_outputs"
    os.makedirs(outdir, exist_ok=True)

    # show and save the copy-pasteable table
    df = pd.DataFrame(table_rows, columns=["Gate", "Matrix", "Effect", "Bloch Sphere Effect"])
    print("\n--- Quantum Gates Reference Table ---\n")
    print(df.to_markdown(index=False))
    df.to_csv(os.path.join(outdir, "quantum_gates_table.csv"), index=False)
    with open(os.path.join(outdir, "quantum_gates_table.md"), "w", encoding="utf8") as f:
        f.write(df.to_markdown(index=False))

    # Compute Bloch vectors for the 6 example single-qubit gates applied to |0>
    ket0 = np.array([1, 0], dtype=complex)
    gates = [("Hadamard (H)", H), ("Phase (S)", S), ("T Gate", T),
             ("Rx(pi/2)", Rx90), ("Ry(pi/2)", Ry90), ("Rz(pi/2)", Rz90)]
    summary = []
    for name, G in gates:
        new_state = G @ ket0
        r = bloch_vector(new_state)
        summary.append((name, r))
        # save single image
        fig = plt.figure(figsize=(4,4))
        ax = fig.add_subplot(111, projection='3d')
        plot_bloch_on_ax(ax, r, title=name)
        fname = os.path.join(outdir, f"{name.replace(' ', '_').replace('(', '').replace(')', '')}.png")
        plt.savefig(fname, dpi=200, bbox_inches='tight')
        plt.close(fig)

    # Combined grid
    fig = plt.figure(figsize=(12, 6))
    for i, (name, r) in enumerate(summary, start=1):
        ax = fig.add_subplot(2, 3, i, projection='3d')
        plot_bloch_on_ax(ax, r, title=name)
    combined_path = os.path.join(outdir, "combined_bloch_grid.png")
    plt.tight_layout()
    plt.savefig(combined_path, dpi=200, bbox_inches='tight')
    plt.close(fig)

    # Save numeric summary
    summary_df = pd.DataFrame([(n, list(r.round(4))) for n, r in summary], columns=["Gate", "Bloch Vector [rx, ry, rz]"])
    summary_df.to_csv(os.path.join(outdir, "bloch_vectors_summary.csv"), index=False)

    print("\nSaved outputs in directory:", outdir)
    print(" - individual PNGs for each gate")
    print(" - combined_bloch_grid.png")
    print(" - quantum_gates_table.csv and quantum_gates_table.md")
    print(" - bloch_vectors_summary.csv\n")
    print("If you use VS Code's Jupyter/Interactive window, you can open the PNGs or examine the CSVs directly.\n")

if __name__ == "__main__":
    main()
