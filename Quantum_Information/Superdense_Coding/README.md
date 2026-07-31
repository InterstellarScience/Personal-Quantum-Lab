## Project: Quantum Teleportation

### 1. Project Goal

The project goal was to study the superdense coding protocol and how to implement it using Qiskit.

### 2. Background & Theory

Superdense coding is another quantum communication protocol, which is less useful than quantum teleportation, since phyisically transmitting qubits is quite challenging and classical communication is already quite inexpensive. It is used when Alice wants to transmit two classical bits $c_0$ and $c_1$ to Bob using the shared, conventional $|\Phi^+\rangle$ e-bit. Depending on which classical bits Alice wants to encode, she has to apply different operations on her Bell pair as follows:

| $c_0$ $c_1$   | operation |
|---------------|-----------|
|     00        | identity  |
|     01        | Z gate    |
|     10        | X gate    |
|     11        | XZ gate   |

which encodes the information into following Bell states:

$(I \otimes I)|\Phi^+\rangle = |\Phi^+\rangle$

$(I \otimes Z)|\Phi^+\rangle = |\Phi^-\rangle$

$(I \otimes X)|\Phi^+\rangle = |\Psi^+\rangle$

$(I \otimes XZ)|\Phi^+\rangle = |\Psi^-\rangle$.  (The notation used here follows the IBM Quantum convention, where Alice's local operations are written on the second tensor factor of the Bell state.

Alice's qubit is then physically transmitted to Bob through a quantum channel, where Bob decodes the message by applying a CNOT operation, followed by a Hadamard operation on the Bell state and then measuring each qubit, returning the initial classical bits.


### 3. Implementation



### 4. Results



### 5. How to run the code



### 6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

### 7. Skills learned
- Learned and implemented the superdense coding protocol.
- Understood how shared entanglement can be used to transmit two classical bits by sending a single qubit.
- Applied Pauli X and Z gates to encode classical information into Bell states.
- Decoded Bell states using CNOT and Hadamard gates.
- Interpreted measurement results and verified successful classical message transmission.
- Organised quantum circuits into reusable Python functions.
