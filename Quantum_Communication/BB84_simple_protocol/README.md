## Project: Bell States

### 1. Project Goal

The project goal was to study and implement practically the BB84 simple protocol, without noise or an eavesdropper interfering with the procedure.

### 2. Background & Theory

The BB84 protocol is a quantum key distribution (QKD) protocol that allows two parties, Alice and Bob, to generate a shared secret key.

Alice first generates a random list of classical bits and a random list of encoding bases. The classical bits can take the values 0 and 1, whereas the encoding bases can be either the computational $Z$ basis or the diagonal $X$ basis.

The four possible combinations are shown below:

| Classical bit | Encoding basis | Quantum state |
|:-------------:|:--------------:|:-------------:|
| 0 | $Z$ | $\lvert 0\rangle$ |
| 1 | $Z$ | $\lvert 1\rangle$ |
| 0 | $X$ | $\lvert +\rangle$ |
| 1 | $X$ | $\lvert -\rangle$ |

The diagonal basis states are defined as:

$$
\lvert +\rangle
=
\frac{1}{\sqrt{2}}
\left(\lvert 0\rangle+\lvert 1\rangle\right)
$$

and:

$$
\lvert -\rangle
=
\frac{1}{\sqrt{2}}
\left(\lvert 0\rangle-\lvert 1\rangle\right).
$$

Bob does not know the encoding bases chosen by Alice and therefore generates his own random list of measurement bases. If Alice and Bob choose the same basis, Bob obtains Alice's classical bit with certainty for an ideal system. On the other hand, if their bases are different, Bob obtains a random measurement result.

After the transmission and measurement of the qubits, Alice and Bob publicly compare their chosen bases without revealing their classical bits. The positions for which the bases did not match are discarded. The remaining bits form the sifted key shared between Alice and Bob.

### 3. Implementation

The implementation follows the theory given above. Alice first generates a random list of classical bits and a random list of encoding bases, where 0 represents the $Z$ basis and 1 represents the $X$ basis.

Each qubit in the Qiskit quantum circuit is initially prepared in the state $\lvert 0\rangle$. Depending on Alice's classical bit and encoding basis, the Identity, Pauli-X, Hadamard and Pauli-Z gates are applied to prepare the corresponding BB84 quantum state.

Bob then generates his own random list of measurement bases. If Bob chooses the $Z$ basis, the corresponding qubit is directly measured. If Bob chooses the $X$ basis, a Hadamard gate is first applied before performing the measurement.

The circuit is simulated using the Qiskit Aer simulator with one shot, since each qubit is only transmitted and measured once in the BB84 protocol. The measurement result is then converted into Bob's classical bit list.

Finally, Alice's and Bob's bases are compared. The bits corresponding to different bases are discarded, whereas the bits corresponding to matching bases are added to the respective sifted keys. For the ideal BB84 protocol, Alice's and Bob's sifted keys are expected to be identical.

This implementation considers the simple ideal case without the presence of an eavesdropper, quantum-channel noise, photon loss, error correction or privacy amplification.

### 4. Results

The results show that the sift keys are the same for both Alice and Bob, meaning that the protocol was indeed successful.

### 5. How to run the code

Simply running the code with the desired number of qubits involved in the simulation to input by the user.

### 6. References / Further readings

Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information (10th Anniversary ed.). Cambridge University Press.

IBM Quantum. Qiskit Documentation. https://quantum.cloud.ibm.com/docs

Qiskit Documentation. https://docs.quantum.ibm.com

### 7. Skills learned
- BB84 quantum-state preparation using the computational \(Z\) basis and diagonal \(X\) basis.
- Quantum-state encoding using Identity, Pauli-X, Hadamard, and Pauli-Z gates.
- Extraction and correct ordering of classical measurement results from Qiskit.
- Basis comparison and key sifting.
- Generation and verification of a shared sifted key between Alice and Bob.
