// Generated from Cirq v1.5.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1)]
qreg q[2];
creg m_c[2];


h q[0];
cx q[0],q[1];

// Gate: cirq.MeasurementGate(2, cirq.MeasurementKey(name='c'), ())
measure q[0] -> m_c[0];
measure q[1] -> m_c[1];
