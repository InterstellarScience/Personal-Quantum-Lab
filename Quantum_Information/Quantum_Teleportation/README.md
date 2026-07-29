Project: Quantum Teleportation

1. Project Goal

The project goal was to study the quantum information protocol quantum teleportation and how to implement it using Qiskit.

2. Background & Theory

Quantum teleportation is one of the first quantum communication protocols invented. It is used to transmit an unknown quantum state from Alice's qubit q0 to another quantum state from Bob's qubit q2. This process goes as follows: 

- The unknown qubit q0 is prepared via a universal single-qubit gate (U gate) and (Alice, Bob) need to be entangled with each other by the Bell state $$|\Phi^+\rangle$$ (by convention), where Alice's half is q1 and Bob's half is q2.
  
- The CNOT gate is applied to q0, directly followed by the Hadamard gate to create the Bell basis.

- Both q0 and q1 are then measured, giving two classical bits 0 and/or 1.

- Bob uses theses classical bits to apply either the identity operator (in case it's 0) or the NOT-and-Z gates.

- Finally, Bob uses the inverse of the U gate to get the initial unknown state Alice had.
  

3. Implementation



4. Results



5. How to run the code



6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

7. Skills learned
