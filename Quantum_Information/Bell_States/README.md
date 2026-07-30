## Project: Bell States

### 1. Project Goal

The project goal was to study Bell states and how to generate them using Qiskit simulations.

### 2. Background & Theory

Bell states are four maximally entangled two-qubit states. There are in total 4 possible Bell states which are:


$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}\left(|00\rangle + |11\rangle\right)
$$

$$
|\Phi^-\rangle = \frac{1}{\sqrt{2}}\left(|00\rangle - |11\rangle\right)
$$

$$
|\Psi^+\rangle = \frac{1}{\sqrt{2}}\left(|01\rangle + |10\rangle\right)
$$

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|01\rangle - |10\rangle\right)
$$

The most general way of creating a Bell state is by first using a Hadamard operation on a qubit and secondly, by using the first qubit as the control qubit towards a target qubit for the CNOT operation. This creates the $|\Phi^+\rangle$ Bell state, which can be changed into the other 3 Bell states by various operations such as the Pauli-X and Pauli-Z operators, or even by a combination of both.

### 3. Implementation

The code starts off by importing the necessary packages such as Qiskit and Matplotlib and preparing the code to save the future results using the Path(__file__).resolve() function. A create_bell_state function is developed, which creates the desired Bell state. The simulate_bell_state function simulates the quantum circuit and measures the qubits, whilst checking the statevectors. It also creates the histogram with the counts of each measurement outcome and plots the quantum circuit. The for loop simply executes the program for all Bell states. 

### 4. Results

The results show clearly that each Bell state has a 50/50 distribution between its two possible measurement outcomes. The statevector confirms the relative phase of each Bell state and the histogram shows clearly the expected measurement probabilities.

### 5. How to run the code

Simply running the code without adding or removing anything will execute the program and save the results.

### 6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

### 7. Skills learned
- Bell state preparation using a Hadamard and a CNOT gate.
- Pauli-X and Pauli-Z transformations.
- Quantum circuit simulation with Qiskit Aer and the basics of Qiskit coding.
- Statevector verification.
- Measurement statistics using repeated shots.
- Python functions and code organization.
