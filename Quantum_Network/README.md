# Quantum Network Simulations

## 1. Overview

This folder contains my quantum network simulations and practical exercises. The purpose of these projects is to study how quantum communication protocols can be implemented between separate quantum network nodes and how quantum and classical communication are combined within the same protocol.

The work included in this folder is mainly based on the course *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators*. The applications are used as practical implementations of the theoretical concepts studied during the course and as part of my wider Personal Quantum Lab.

Some of the starting applications were cloned from the Quantum Network Explorer (QNE) repository using the QNE application clone functionality. These applications were then executed, investigated and documented to develop my understanding of their physical principles and computational implementation. Any project based on provided QNE code is identified within its individual README file.

## 2. Project Goal

The overall goal of this folder is to develop a practical understanding of quantum networks by studying the communication between multiple quantum nodes.

The individual projects investigate concepts such as:

- The generation and distribution of entangled qubit pairs.
- Quantum and classical communication between remote nodes.
- Quantum teleportation.
- Quantum state preparation, measurement and reconstruction.
- The influence of quantum measurement on distributed protocols.
- The verification of quantum communication protocols using density matrices and state fidelity.

These projects connect the mathematical description of quantum information with its implementation in a simulated quantum network. The focus is therefore not only on obtaining a working simulation, but also on understanding why each quantum gate, measurement and classical message is required.

## 3. Quantum Network Framework

A quantum network consists of multiple nodes which can exchange quantum and classical information. Quantum channels can be used to distribute quantum states or entanglement, whereas classical channels are used to exchange ordinary classical data.

The quantum protocols investigated in this folder generally combine both types of communication. Entanglement provides correlations which cannot be reproduced by a classical system, while classical communication allows the different nodes to coordinate their operations and interpret their measurement results.

This can be represented by the following general process:

1. A quantum resource, such as an entangled pair, is generated between two nodes.
2. Local quantum operations are applied at each node.
3. One or more qubits are measured.
4. The measurement results are exchanged through a classical channel when required.
5. The receiving node uses the obtained information to complete or verify the protocol.

The exact order and purpose of these operations depend on the investigated quantum communication protocol.

## 4. Tools and Technologies

The simulations use the following tools:

| Tool | Purpose |
|:---|:---|
| Python | Used to implement the application logic for the individual quantum network nodes. |
| Quantum Network Explorer (QNE) | Provides the application development environment and examples for quantum network applications. |
| QNE-ADK | Provides the command-line tools used to create, clone, validate and run applications and experiments. |
| NetQASM | Provides the software interface used to describe quantum operations and communicate with a quantum network backend. |
| SquidASM | Connects NetQASM applications to the NetSquid simulation backend. |
| NetSquid | Simulates the quantum network, its nodes and the communication between them. |

NetQASM acts as the interface between the application code and the simulated quantum network processor. SquidASM then allows the NetQASM application to be executed using NetSquid. NetSquid finally simulates the behaviour of the quantum network and returns the results of the experiment.

## 5. Repository Structure

Each quantum network application is stored within its own project folder. The individual folders can contain:

- The source code for each quantum network node.
- Application and network configuration files.
- Experiment configurations and inputs.
- Simulation results.
- A separate README explaining the theory, implementation and obtained results.

The current projects include:

| Project | Description |
|:---|:---|
| Quantum teleportation | Teleportation of an arbitrary single-qubit state between a sender and receiver using an entangled pair and two classical correction bits. |
| Entanglement distribution | Generation of an EPR pair between two network nodes and measurement of the resulting correlations. |

Further quantum network applications will be added as I progress through the course and continue developing the Personal Quantum Lab.

## 6. Running an Experiment

The required Python virtual environment must first be activated. This environment contains QNE-ADK, NetQASM, SquidASM and NetSquid.

An experiment can then be executed from the parent directory using

```bash
qne experiment run EXPERIMENT_NAME
```

The results can be displayed using

```bash
qne experiment results EXPERIMENT_NAME
```

`EXPERIMENT_NAME` must be replaced by the name of the relevant experiment. Additional configuration requirements are described within the README file of each individual project.

## 7. Learning Outcomes

The projects within this folder develop the following skills:

- Implementation of applications containing multiple quantum network nodes.
- Creation of quantum and classical sockets between remote nodes.
- Entanglement generation and distribution using EPR sockets.
- Programming of local quantum gates and measurements using NetQASM.
- Execution of distributed quantum protocols using NetSquid simulations.
- Interpretation of probabilistic quantum measurement results.
- Verification of transmitted or reconstructed states using density matrices and fidelity.
- Understanding of the different roles of quantum channels, classical channels and shared entanglement.

## 8. Course and Attribution

The projects in this folder are mainly based on the course *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators*.

Some applications originate from examples provided by the Quantum Network Explorer and QuTech contributors and were obtained using the QNE clone functionality. These examples are used here for educational purposes to study their implementation and underlying physics. The corresponding attribution and any modifications are described separately for each project.

## 9. References

- [Quantum Network Explorer](https://www.quantum-network.com/)
- [NetQASM](https://github.com/QuTech-Delft/netqasm)
- [SquidASM](https://github.com/QuTech-Delft/squidasm)
- [NetSquid](https://netsquid.org/)
