Project: Quantum Teleportation

1. Project Goal

The project goal was to study the quantum information protocol quantum teleportation and how to implement it using Qiskit.

2. Background & Theory

Quantum teleportation is one of the first quantum communication protocols invented. . It enables the transmission of an unknown quantum state from Alice's qubit (q_0) to Bob's qubit (q_2), without physically sending the qubit itself. The protocol requires a shared entangled Bell pair and the exchange of two classical bits of information.

The protocol proceeds as follows:

An arbitrary quantum state is prepared on Alice's qubit (q_0) using the universal single-qubit gate (U(\theta,\phi,\lambda)). Alice and Bob also share an entangled Bell pair, conventionally prepared in the Bell state
$$|\Phi^+\rangle=\frac{1}{\sqrt{2}}\left(|00\rangle+|11\rangle\right)$$
where (q_1) belongs to Alice and (q_2) belongs to Bob.
Alice applies a CNOT gate with (q_0) as the control qubit and (q_1) as the target qubit, followed by a Hadamard gate on (q_0). These operations transform Alice's two qubits into the Bell basis.
Alice measures both (q_0) and (q_1), producing two classical bits that are transmitted to Bob through a classical communication channel.
Depending on the received classical bits, Bob applies the appropriate correction operation to (q_2). The possible corrections are the identity ((I)), (X), (Z), or (XZ). After this step, Bob's qubit is in exactly the same unknown quantum state that was initially prepared on Alice's qubit.
In this project, the teleportation is verified by applying the inverse of the original state-preparation gate, (U^\dagger), to Bob's qubit. Since (U^\dagger U|0\rangle = |0\rangle), measuring Bob's qubit in the computational basis should always yield the state (|0\rangle), confirming successful teleportation.
  

3. Implementation



4. Results



5. How to run the code



6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

7. Skills learned
