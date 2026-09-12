# Quantum Networks

## 1. Project Goal

The project goal of this folder is to study quantum networks and quantum communication protocols using NetQASM and NetSquid simulations.

The projects are mainly from the *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators* course. They are also part of my Personal Quantum Lab, where I am using the theory that I learned from my courses and apply it to practical quantum simulations.

The main purpose is to understand how different quantum nodes can communicate with each other, and how entanglement can be created and shared between them. The projects are also investigating how quantum communication and classical communication are both required for protocols such as quantum teleportation.

Some of the applications were cloned from the Quantum Network Explorer (QNE) using their clone function. When this is the case, it is mentioned in the README of the corresponding project. The goal for these applications was to understand the code, run the simulation and analyse what is happening between the different nodes.

## 2. Background & Theory

A quantum network is a network which connects different quantum nodes with each other. These nodes can contain their own qubits and can perform local quantum operations such as quantum gates and measurements.

There are in total two main types of communications used for the projects, which are quantum communication and classical communication.

The quantum communication is used for sharing quantum information or entanglement between the nodes. The classical communication is instead used for sending classical values, such as the results obtained after measuring a qubit.

For example, two nodes called Alice and Bob can share the following Bell state:

$$
\lvert \Phi^+ \rangle = \frac{1}{\sqrt{2}}\left(\lvert 00 \rangle + \lvert 11 \rangle\right).
$$

Alice has one of the two qubits, whereas Bob has the other qubit. If they both measure their qubits in the computational basis, they will either both measure $0$ or both measure $1$. The individual result is random, but the results between Alice and Bob are correlated due to their shared entangled state.

However, the entanglement alone cannot be used to send a classical message. The result obtained by Alice is random and she cannot choose whether she measures $0$ or $1$. A classical channel is therefore still required when Alice needs to send a specific information to Bob.

This combination between quantum and classical communications is one of the main ideas investigated within this folder.

## 3. Software Used

The projects were written in Python and are using the Quantum Network Explorer Application Development Kit (QNE-ADK), NetQASM, SquidASM and NetSquid.

QNE-ADK is used to create or clone the quantum applications and to create the experiments. It is also used to run the experiments from the terminal.

NetQASM is used to write the programs of the different quantum nodes. For example, Alice and Bob each have their own Python program, while both programs are part of the same quantum network application.

The `EPRSocket` is used to create entanglement between two quantum nodes. On the other hand, a classical `Socket` is used when the nodes need to send classical information to each other.

SquidASM is used to connect the NetQASM application to NetSquid, whereas NetSquid is used to simulate the quantum network and its different nodes.

The different tools can therefore be summarised as:

$$
\text{QNE-ADK} \rightarrow \text{NetQASM} \rightarrow \text{SquidASM} \rightarrow \text{NetSquid}.
$$

## 4. Projects

The folder currently includes the following projects:

### 4.1 EPR Pair between Alice and Bob

The first project creates an EPR pair between Alice and Bob. Alice creates the entangled pair and keeps one qubit, whereas Bob receives the second qubit. Both qubits are then measured in the computational basis to verify their correlated results.

### 4.2 Quantum Teleportation

The second project investigates the quantum teleportation protocol. An arbitrary quantum state is teleported from a sender to a receiver using a shared entangled pair and two classical bits.

The sender first prepares the state and performs the required CNOT and Hadamard operations. The two qubits of the sender are then measured and the obtained results are sent to the receiver through a classical channel. Depending on these results, the receiver performs the required Pauli-$X$ and Pauli-$Z$ corrections to recover the initial state.

The fidelity between the initial and the received state is finally calculated to verify the quantum teleportation simulation.

Further projects will be added to this folder while progressing through the course.

## 5. Running the Experiments

The simulations are run inside a Python virtual environment containing the required quantum network packages.

An experiment can be run using:

```bash
qne experiment run EXPERIMENT_NAME
```

The results can then be shown using:

```bash
qne experiment results EXPERIMENT_NAME
```

where `EXPERIMENT_NAME` needs to be replaced by the name of the corresponding experiment.

## 6. Skills Learned

- The structure of a quantum network.
- Quantum nodes and local quantum operations.
- Entanglement creation between different nodes.
- Quantum and classical communications.
- EPR sockets and classical sockets.
- Quantum circuit simulations using NetQASM and NetSquid.
- Quantum teleportation between two quantum nodes.
- Density matrices and fidelity verification.
- The basics of QNE applications and experiments.
- Python functions and code organisation.

## 7. Course & Attribution

The projects in this folder are mainly based on the *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators* course.

Some of the starting applications were cloned from the Quantum Network Explorer and were provided by QNE and QuTech. These applications are used for learning purposes and to understand how the corresponding quantum network protocols are simulated.

## 8. References

- [Quantum Network Explorer](https://www.quantum-network.com/)
- [NetQASM](https://github.com/QuTech-Delft/netqasm)
- [SquidASM](https://github.com/QuTech-Delft/squidasm)
- [NetSquid](https://netsquid.org/)
