# Quantum Teleportation using NetQASM and NetSquid

## 1. Project Goal

The project goal was to study the quantum teleportation protocol and simulate the transfer of an arbitrary single-qubit state between two quantum-network nodes using NetQASM, SquidASM and the NetSquid simulator.

The application contains two nodes called `sender` and `receiver`. The sender prepares the quantum state, performs the teleportation measurements and sends two classical correction bits to the receiver. The receiver then applies the required quantum gates to reconstruct the original state.

This application was cloned from the Quantum Network Explorer (QNE) repository using the QNE clone function. The purpose of the project was therefore to run, study and understand the provided implementation rather than claiming the original application code as my own.

## 2. Background & Theory

Quantum teleportation transfers an unknown quantum state from one location to another using one shared entangled pair and two bits of classical information. The physical qubit itself is not transported from the sender to the receiver.

The state prepared by the sender can be written as

$$
\lvert \psi \rangle = \cos\left(\frac{\theta}{2}\right)\lvert 0 \rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)\lvert 1 \rangle.
$$

The sender and receiver also share an entangled Bell pair,

$$
\lvert \Phi^+ \rangle = \frac{1}{\sqrt{2}}\left(\lvert 00 \rangle + \lvert 11 \rangle\right).
$$

The sender applies a CNOT gate between the state qubit and the local half of the entangled pair. A Hadamard gate is then applied to the state qubit before both local qubits are measured. These measurements produce the two classical bits $m_1$ and $m_2$.

The receiver uses these bits to determine the required corrections:

| $m_1$ | $m_2$ | Receiver correction |
|---:|---:|:---|
| 0 | 0 | No correction |
| 0 | 1 | $X$ |
| 1 | 0 | $Z$ |
| 1 | 1 | $ZX$ |

The recovered state is therefore

$$
\lvert \psi_{\mathrm{receiver}} \rangle = Z^{m_1}X^{m_2}\lvert \psi_{\mathrm{uncorrected}} \rangle.
$$

After the corrections are applied, the receiver's qubit corresponds to the original state $\lvert\psi\rangle$. The original state is destroyed by the sender's measurements, and therefore the protocol does not copy an unknown quantum state and does not violate the no-cloning theorem.

Entanglement alone does not transmit usable information instantaneously. The receiver must obtain the classical measurement results before the correct state can be reconstructed. Consequently, quantum teleportation does not enable faster-than-light communication.

## 3. Implementation

The simulation is divided into a sender program and a receiver program.

### Sender

The sender performs the following operations:

1. Creates a classical socket to the receiver.
2. Creates an EPR socket for entanglement generation.
3. Prepares a qubit using the input angles $\phi$ and $\theta$.
4. Creates an entangled pair and shares one half with the receiver.
5. Applies the CNOT and Hadamard gates required by the teleportation protocol.
6. Measures both local qubits to obtain $m_1$ and $m_2$.
7. Sends the two classical measurement results to the receiver.

The input values are treated as coefficients of $\pi$. For example, an input of `phi = 0.5` represents $\phi=0.5\pi$.

### Receiver

The receiver performs the following operations:

1. Receives the second half of the entangled pair.
2. Receives the classical measurement results $m_1$ and $m_2$.
3. Applies an $X$ correction when $m_2=1$.
4. Applies a $Z$ correction when $m_1=1$.
5. Retrieves the reconstructed state when the NetSquid simulator is used.
6. Calculates the fidelity between the original state and the teleported state.

The original values of $\phi$ and $\theta$ are additionally sent through a silent classical message only for simulation and visualisation. This information is not required by the physical teleportation protocol and would not normally be available to the receiver.

## 4. Fidelity Verification

The success of the simulation is verified using the state fidelity,

$$
F = \langle\psi\rvert\rho_{\mathrm{receiver}}\lvert\psi\rangle,
$$

where $\lvert\psi\rangle$ is the original pure state and $\rho_{\mathrm{receiver}}$ is the density matrix of the reconstructed state. For an ideal and noiseless teleportation process, the expected fidelity is

$$
F=1.
$$

A fidelity equal to one means that the state reconstructed by the receiver is identical to the state originally prepared by the sender.

## 5. Technologies Used

- Python
- Quantum Network Explorer Application Development Kit (QNE-ADK)
- NetQASM
- SquidASM
- NetSquid

## 6. Running the Simulation

Activate the virtual environment containing QNE, NetQASM, SquidASM and NetSquid. The experiment can then be executed from the parent project directory using

```bash
qne experiment run my_exp
```

After a successful run, the results can be inspected using

```bash
qne experiment results my_exp
```

The exact command may depend on the names assigned to the local application and experiment.

## 7. Expected Results

The output contains:

- The two measurement results produced by the sender.
- The $X$ and/or $Z$ corrections applied by the receiver.
- The density matrix of the original state.
- The density matrix of the reconstructed state.
- The fidelity between the two states.

For an ideal simulation, the original and received density matrices should agree and the fidelity should be approximately equal to one.

## 8. Skills Learned

- The physical steps of the quantum teleportation protocol.
- State preparation using the Bloch-sphere angles $\theta$ and $\phi$.
- Entanglement generation between two quantum-network nodes.
- Quantum and classical socket communication using NetQASM.
- The use of CNOT, Hadamard, Pauli-$X$ and Pauli-$Z$ gates.
- The role of classical measurement bits in quantum teleportation.
- Density-matrix inspection and fidelity verification using NetSquid.
- The distinction between transferring a quantum state and physically transporting a qubit.

## 9. Attribution

The starting application was cloned from the Quantum Network Explorer example repository through the QNE-ADK clone functionality. The original implementation and supporting framework were developed by the Quantum Network Explorer and QuTech contributors. This repository documents my execution, study and understanding of the quantum teleportation simulation.

## 10. References

- [Quantum Network Explorer](https://www.quantum-network.com/)
- [NetQASM](https://github.com/QuTech-Delft/netqasm)
- [SquidASM](https://github.com/QuTech-Delft/squidasm)
