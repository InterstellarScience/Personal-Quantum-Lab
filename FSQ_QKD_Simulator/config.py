import qiskit as qk
import numpy as np

# Create quantum circuit for single qubit
def prepare_single_qubit(bit, basis):
    # Create quantum circuit
    qc = qk.QuantumCircuit(1,1)

    #Z-basis check
    if bit == 0 and basis == 0:
        qc.id(0)
    
    if bit == 1 and basis == 0:
        qc.x(0)
    
    #X-basis check
    if bit == 0 and basis == 1:
        qc.h(0)
    
    if bit == 1 and basis == 1:
        qc.h(0)
        qc.z(0)

    return (qc)

prepare_single_qubit(np.random.randint(0,2),np.random.randint(0,2))