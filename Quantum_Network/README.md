# Quantum Network

## 1. Project Goal

The goal of this folder is to study quantum networks and how quantum communication protocols can be simulated using Python, NetQASM and NetSquid.

The projects included in this folder are mainly based on the *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators* course. They are part of my Personal Quantum Lab and are used to improve my understanding of quantum communication and quantum networks through practical simulations.

The applications are used to investigate how two or more quantum network nodes can communicate with each other using quantum and classical channels. This includes the generation of entanglement between separated nodes, the local manipulation of qubits and the exchange of classical information.

Some of the applications were cloned from the Quantum Network Explorer (QNE) repository using the QNE clone function. The purpose of these projects is therefore to study, run and understand the provided applications and the physics behind them. The individual project READMEs specify when an application was cloned from QNE.

## 2. Background & Theory

A quantum network consists of different quantum nodes which are connected through quantum and classical channels.

The quantum channels are used to distribute qubits or entanglement between the nodes. On the other hand, the classical channels are used to exchange classical information such as measurement results. Most quantum communication protocols require both channels to perform the complete protocol.

One of the main resources of a quantum network is entanglement. For example, two nodes called Alice and Bob can share the Bell state

$$
\lvert \Phi^+ \rangle = \frac{1}{\sqrt{2}}\left(\lvert 00 \rangle + \lvert 11 \rangle\right).
$$

Alice possesses the first qubit of the state, whereas Bob possesses the second qubit. Although the qubits are located at different nodes, their measurement results remain correlated.

However, entanglement does not allow classical information to be sent faster than light. Classical communication is still required whenever the receiver needs to know the measurement result or operation performed by the sender.

The simulations in this folder are therefore used to study the relation between the following parts of a quantum network:

- Quantum nodes.
- Local qubits.
- Quantum gates and measurements.
- Entanglement generation and distribution.
- Quantum channels.
- Classical channels.
- Quantum and classical sockets.

## 3. Software & Simulation Framework

The simulations use different software tools which are connected to each other.

### 3.1 Quantum Network Explorer

The Quantum Network Explorer (QNE) provides quantum network applications, network configurations and tools to create and run quantum network experiments.

The QNE Application Development Kit (QNE-ADK) is used through the terminal. It allows applications and experiments to be created, cloned, validated and simulated.

### 3.2 NetQASM

NetQASM is used to write the individual program of each quantum network node. It provides the instructions required to create qubits, apply quantum gates, measure qubits and communicate with other nodes.

An `EPRSocket` is used for the generation and distribution of entangled qubit pairs. A classical `Socket` is instead used to send classical information between the nodes.

### 3.3 SquidASM

SquidASM connects the NetQASM applications to the NetSquid simulator. It therefore allows the programs written for the individual nodes to be executed together as one quantum network application.

### 3.4 NetSquid

NetSquid is the simulator which simulates the quantum network, the quantum nodes and their connections. It is also used to obtain simulation-specific information such as the density matrix of a qubit and the fidelity between quantum states.

The general relation between the software tools is therefore:

$$
\text{QNE-ADK} \rightarrow \text{NetQASM} \rightarrow \text{SquidASM} \rightarrow \text{NetSquid}.
$$

## 4. Projects

The folder currently contains the following projects:

| Project | Description |
|:---|:---|
| Entanglement distribution | Generation of an EPR pair between two quantum network nodes and measurement of both entangled qubits. |
| Quantum teleportation | Teleportation of an arbitrary single-qubit state from a sender to a receiver using one shared entangled pair and two classical bits. |

Further quantum network applications will be added while progressing through the course.

Each project folder contains the source code of the different quantum network nodes, the required configuration files and the experiment files. A separate README is also included to explain the goal, theory and implementation of the corresponding project.

## 5. Running the Simulations

The simulations are run inside a Python virtual environment containing QNE-ADK, NetQASM, SquidASM and NetSquid.

An experiment can be run from the `Quantum_Network` folder using

```bash
qne experiment run EXPERIMENT_NAME
```

where `EXPERIMENT_NAME` is replaced by the name of the experiment.

The results can then be displayed using

```bash
qne experiment results EXPERIMENT_NAME
```

The exact application inputs and network configurations depend on the investigated project.

## 6. Skills Learned

- The structure of a quantum network and its different nodes.
- The difference between quantum and classical communication channels.
- Entanglement generation and distribution between separated nodes.
- Quantum and classical socket communication.
- Quantum circuit simulations using NetQASM and NetSquid.
- The basics of QNE applications and experiments.
- The use of the QNE-ADK command-line interface.
- Quantum state preparation and measurement.
- Density matrix and quantum state fidelity verification.
- Python functions and code organisation for distributed quantum applications.

## 7. Course & Attribution

The projects are mainly based on the *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators* course.

Some of the applications were cloned from the Quantum Network Explorer repository and were originally developed by the Quantum Network Explorer and QuTech contributors. These applications are used for educational purposes to understand their code, simulation and physical principles.

## 8. References

- [Quantum Network Explorer](https://www.quantum-network.com/)
- [NetQASM](https://github.com/QuTech-Delft/netqasm)
- [SquidASM](https://github.com/QuTech-Delft/squidasm)
- [NetSquid](https://netsquid.org/)
