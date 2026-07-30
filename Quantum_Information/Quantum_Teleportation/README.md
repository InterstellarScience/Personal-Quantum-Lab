Project: Quantum Teleportation

1. Project Goal

The project goal was to study the quantum information protocol quantum teleportation and how to implement it using Qiskit.

2. Background & Theory

Quantum teleportation is one of the first quantum communication protocols invented. It is used to transmit an unknown quantum state from Alice's qubit $q_0$ to Bob's qubit $q_2$, without physically sending the qubit itself. This process goes as follows:

- The unknown qubit $q_0$ is prepared using the universal single-qubit gate (U gate), defined as $U(\theta,\phi,\lambda)=R_{z}(\theta)R_{y}(\phi)R_{z}(\lambda)$. Alice and Bob also share an entangled Bell state, which is conventionally chosen as $$|\Phi^+\rangle$$, with Alice's half of the Bell pair being $q_1$ and Bob's half being $q_2$.

- A CNOT gate is applied with $q_0$ as the control qubit and $q_1$ as the target qubit, followed by a Hadamard gate on $q_0$ to transform Alice's qubits into the Bell basis.

- Both $q_0$ and $q_1$ are then measured, producing two classical bits (0 or 1), which are sent to Bob via classical communication.

- Bob uses these classical bits to apply the appropriate correction operation to $q_2$: either the identity operator, the (X) gate, the (Z) gate, or both (X) and (Z), depending on Alice's measurement outcomes.

- In this project, the teleportation is verified by applying the inverse of the original U gate to Bob's qubit. Since $U^\dagger U|0\rangle = |0\rangle$, measuring Bob's qubit should always return the state $|0\rangle$, confirming that the teleportation was a success. In a real quantum computer, the result wouldn't be always $|0\rangle$ but it could also be $|1\rangle$ indicating that noise might interfere with the quantum teleportation protocol.

  

3. Implementation

The implementation follows the protocol described in the Background & Theory section. First, the unknown quantum state is prepared on Alice's qubit using the U gate. Afterwards, the Bell pair is created between Alice's and Bob's qubits. Alice then performs the Bell-basis measurement, after which Bob applies the corresponding correction gates depending on the received classical bits. Finally, the teleportation is verified using the method described in the last paragraph of the Background & Theory section.

4. Results

The results from the circuit in the image folder, shows for a simulation of n = 1024 measurement counts, the following: 

{'001': 241, '010': 265, '011': 250, '000': 268}, 

verifying that Bob's qubit is measured in the state $|0\rangle$, which clearly shows tha the teleportation was a success. The four possible measurement outcomes are also approximately equally distributed.

5. How to run the code

Simply running the code without adding or removing anything will execute the program and save the results. If you wish, you can slightly change the angles $\theta$ and $\phi$ to prepare your preferred quantum state.

6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

7. Skills learned
- Preparing arbitrary single-qubit states using the universal U gate.
- Learning and implementing the quantum teleportation protocol.
- Using classical conditional operations (if_test) in Qiskit.
- Understanding the role of entanglement and classical communication in quantum teleportation.
- Verifying quantum teleportation using the inverse of the state-preparation gate.
