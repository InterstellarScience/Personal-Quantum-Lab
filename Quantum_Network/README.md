# Quantum Teleportation using NetQASM and NetSquid

## 1. Project Goal

The project goal was to study the quantum teleportation protocol and how to simulate it between two quantum network nodes using NetQASM and NetSquid.

The application was cloned from the Quantum Network Explorer (QNE) repository using the QNE application clone function. The purpose of this project was therefore to study the provided code, run the simulation and understand how quantum teleportation is implemented within a simulated quantum network.

The application consists of two nodes, which are the `sender` and the `receiver`. The sender prepares an arbitrary single-qubit state and teleports it to the receiver using a shared entangled pair and two classical bits. The receiver then applies the required quantum corrections to recover the initial quantum state.

## 2. Background & Theory

Quantum teleportation is a quantum communication protocol which allows an unknown quantum state to be transferred from a sender to a receiver. The physical qubit itself is not transported between the two nodes. Instead, the protocol uses a previously shared entangled pair together with two bits of classical information.

The arbitrary quantum state prepared by the sender can be written as

$$
\lvert \psi \rangle = \cos\left(\frac{\theta}{2}\right)\lvert 0 \rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)\lvert 1 \rangle,
$$

where $\theta$ and $\phi$ determine the position of the state on the Bloch sphere.

The sender and receiver also share one entangled Bell pair. The Bell state used for the protocol is

$$
\lvert \Phi^+ \rangle = \frac{1}{\sqrt{2}}\left(\lvert 00 \rangle + \lvert 11 \rangle\right).
$$

The sender therefore possesses the state qubit and the first qubit of the entangled pair, whereas the receiver possesses the second entangled qubit.

To perform the teleportation, the sender first applies a CNOT gate between the state qubit and the local entangled qubit. A Hadamard gate is then applied to the state qubit. Both qubits are subsequently measured, producing the two classical measurement results $m_1$ and $m_2$.

The two classical bits are sent to the receiver through a classical communication channel. Depending on their values, the receiver applies the following corrections:

| $m_1$ | $m_2$ | Correction applied by the receiver |
|:---:|:---:|:---:|
| 0 | 0 | No correction |
| 0 | 1 | $X$ |
| 1 | 0 | $Z$ |
| 1 | 1 | $ZX$ |

The corrected state of the receiver can therefore be represented as

$$
\lvert \psi_{\mathrm{receiver}} \rangle = Z^{m_1}X^{m_2}\lvert \psi_{\mathrm{uncorrected}} \rangle.
$$

After the required corrections are applied, the receiver recovers the original state $\lvert\psi\rangle$. The original state at the sender is destroyed by the measurements. The quantum state is therefore transferred rather than copied, which is consistent with the no-cloning theorem.

The shared entanglement is not sufficient on its own to complete the protocol. The receiver must also obtain the two classical measurement results before the original state can be recovered. Quantum teleportation therefore does not allow faster-than-light communication.

## 3. Implementation

The quantum teleportation application is divided into a sender program and a receiver program.

### 3.1 Sender

The sender first creates a classical socket to communicate with the receiver and an EPR socket to generate the entangled pair. A connection to the NetQASM backend is then created.

The arbitrary quantum state is prepared using the input parameters $\phi$ and $\theta$. Within the application, these parameters are given as coefficients of $\pi$. For example, `phi = 0.5` corresponds to $\phi=0.5\pi$.

The sender then generates the entangled pair and keeps one of its qubits while the second qubit is shared with the receiver. A CNOT gate is applied between the state qubit and the entangled qubit, followed by a Hadamard gate on the state qubit. Both local qubits are then measured to obtain the classical results $m_1$ and $m_2$.

Finally, the two results are sent to the receiver using the classical socket.

### 3.2 Receiver

The receiver creates a corresponding classical socket and EPR socket before connecting to the NetQASM backend. The receiver then receives its half of the entangled pair and the two classical measurement results sent by the sender.

An $X$ gate is applied when $m_2=1$, while a $Z$ gate is applied when $m_1=1$. If both results are equal to one, both corrections are applied. These operations reconstruct the initial state on the receiver's qubit.

When NetSquid is used as the simulator, the density matrix of the received state is extracted and compared with the density matrix of the original state. The original values of $\phi$ and $\theta$ are also sent through a silent classical message for this verification. This additional transmission is only used for the simulation and visualisation of the results. It is not part of the physical quantum teleportation protocol.

## 4. Fidelity Verification

The fidelity is calculated to verify whether the quantum state was successfully teleported. For an original pure state $\lvert\psi\rangle$ and the received density matrix $\rho_{\mathrm{receiver}}$, the fidelity is given by

$$
F = \langle\psi\rvert\rho_{\mathrm{receiver}}\lvert\psi\rangle.
$$

For an ideal quantum teleportation simulation, the expected result is

$$
F=1.
$$

A fidelity equal to one means that the state obtained by the receiver is identical to the state initially prepared by the sender. The comparison of both density matrices therefore provides a numerical verification of the teleportation protocol.

## 5. Running the Simulation

The required virtual environment must first be activated. The environment contains QNE-ADK, NetQASM, SquidASM and NetSquid.

The experiment can then be run from the parent directory using

```bash
qne experiment run my_exp
```

The obtained results can be displayed using

```bash
qne experiment results my_exp
```

The experiment name `my_exp` can be replaced by the name assigned to the experiment.

## 6. Expected Results

The simulation returns the two classical measurement results obtained by the sender and the quantum corrections applied by the receiver. When the NetSquid simulator is used, it also returns the original density matrix, the received density matrix and their fidelity.

For an ideal and noiseless simulation, the original and received density matrices are expected to be equal, with a fidelity approximately equal to one. The exact values of $m_1$ and $m_2$ can change between individual simulations due to the probabilistic nature of quantum measurement. However, the reconstructed state remains the same after the corresponding corrections are applied.

## 7. Skills Learned

- Quantum teleportation using a shared entangled pair and classical communication.
- Preparation of an arbitrary single-qubit state using $\theta$ and $\phi$.
- Bell state generation and distribution between two quantum network nodes.
- Quantum and classical communication using EPR sockets and classical sockets.
- CNOT and Hadamard operations for the teleportation measurements.
- Pauli-$X$ and Pauli-$Z$ corrections at the receiver.
- Quantum circuit simulation using NetQASM, SquidASM and NetSquid.
- Density matrix extraction and fidelity verification.
- The distinction between the transfer of a quantum state and the physical transfer of a qubit.

## 8. Attribution

The quantum teleportation application was cloned from the Quantum Network Explorer repository using the QNE-ADK clone functionality. The original application and the simulation framework were developed by the Quantum Network Explorer and QuTech contributors. This project presents my study, execution and understanding of the provided quantum teleportation simulation.

## 9. References

- [Quantum Network Explorer](https://www.quantum-network.com/)
- [NetQASM](https://github.com/QuTech-Delft/netqasm)
- [SquidASM](https://github.com/QuTech-Delft/squidasm)
