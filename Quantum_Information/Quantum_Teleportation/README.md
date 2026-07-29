Project: Quantum Teleportation

1. Project Goal

The project goal was to study the quantum information protocol quantum teleportation and how to implement it using Qiskit.

2. Background & Theory

Quantum teleportation is one of the first quantum communication protocols invented. It is used to transmit an unknown quantum state from Alice's qubit $q_0$ to Bob's qubit $q_2$, without physically sending the qubit itself. This process goes as follows:

- The unknown qubit $q_0$ is prepared using the universal single-qubit gate (U gate). Alice and Bob must also share an entangled Bell state, conventionally chosen as $$|\Phi^+\rangle$$, where Alice's half of the Bell pair is $q_1$ and Bob's half is $q_2$.

- A CNOT gate is applied with $q_0$ as the control qubit and $q_1$ as the target qubit, followed by a Hadamard gate on $q_0$ to transform Alice's qubits into the Bell basis.

- Both $q_0$ and $q_1$ are then measured, producing two classical bits (0 or 1), which are sent to Bob through a classical communication channel.

- Bob uses these classical bits to apply the appropriate correction operation to $q_2$: either the identity operator, the (X) gate, the (Z) gate, or both (X) and (Z), depending on Alice's measurement outcomes.

- Finally, in this project, the teleportation is verified by applying the inverse of the original U gate to Bob's qubit. Since $U^\dagger U|0\rangle = |0\rangle$, measuring Bob's qubit should always return the state (|0\rangle), confirming that the teleportation was successful.

  

3. Implementation



4. Results



5. How to run the code



6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

7. Skills learned
