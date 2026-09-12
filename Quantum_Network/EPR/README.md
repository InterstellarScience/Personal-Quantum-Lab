# EPR Pair between Alice and Bob

## 1. Project Goal

The project goal was to create an entangled pair between two quantum network nodes called Alice and Bob using NetQASM and NetSquid simulations.

Alice creates an Einstein--Podolsky--Rosen (EPR) pair and keeps the first qubit, whereas the second qubit is received by Bob. Alice and Bob then measure their individual qubits in the computational basis and return their measurement results.

The purpose of this project was to study how entanglement can be generated and distributed between two separated nodes within a simulated quantum network.

## 2. Background & Theory

An EPR pair consists of two maximally entangled qubits. The two qubits cannot be described independently from each other, even if they are located at two different quantum network nodes.

The EPR pair generated in this project can be represented by the Bell state

$$
\lvert \Phi^+ \rangle = \frac{1}{\sqrt{2}}\left(\lvert 00 \rangle + \lvert 11 \rangle\right).
$$

The state shows that there are in total two possible measurement outcomes when both qubits are measured in the computational basis. Alice and Bob can either both measure $0$, corresponding to the $\lvert 00\rangle$ state, or both measure $1$, corresponding to the $\lvert 11\rangle$ state.

The individual result obtained by Alice is random, with

$$
P(A=0)=P(A=1)=\frac{1}{2}.
$$

The same applies to the individual result obtained by Bob. However, the two results are perfectly correlated:

$$
P(A=B)=1.
$$

The expected joint probabilities for an ideal simulation are therefore

| Alice | Bob | Probability |
|:---:|:---:|:---:|
| 0 | 0 | $1/2$ |
| 0 | 1 | $0$ |
| 1 | 0 | $0$ |
| 1 | 1 | $1/2$ |

The measurement of one qubit therefore determines the possible result of the other qubit. Nevertheless, neither Alice nor Bob can control their individual measurement result. The entanglement can therefore not be used on its own to send classical information faster than light.

## 3. Implementation

The application is divided into two Python programs, which represent the Alice and Bob quantum network nodes.

### 3.1 Alice

Alice first creates an `EPRSocket` which is connected to Bob. The EPR socket is then included within Alice's `NetQASMConnection` to connect the socket to the quantum network backend.

Alice creates the entangled pair using

```python
epr = epr_socket.create_keep()[0]
```

The `create_keep()` instruction creates the EPR pair and returns the qubit which is kept by Alice. Alice then measures her qubit in the computational basis using

```python
m = epr.measure()
```

The result is converted into a classical integer and returned as Alice's result.

### 3.2 Bob

Bob creates a corresponding `EPRSocket` which is connected to Alice. The socket is also included within Bob's `NetQASMConnection`.

Bob receives his half of the entangled pair using

```python
epr = epr_socket.recv_keep()[0]
```

The `recv_keep()` instruction receives the qubit created through Alice's EPR request. The connection is flushed to execute the queued quantum network instructions before Bob measures his qubit in the computational basis.

Bob's measurement result is also converted into a classical integer and returned as Bob's result.

## 4. Expected Results

For each individual experiment, Alice and Bob are expected to obtain one of the following results:

```text
Alice = 0, Bob = 0
```

or

```text
Alice = 1, Bob = 1
```

The exact result changes between different experiments due to the probabilistic nature of quantum measurement. However, the two results should remain equal for an ideal EPR pair when both qubits are measured in the same computational basis.

A single experiment only produces one pair of measurement results. The $50\%$ probability of each correlated outcome becomes visible when the experiment is repeated many times.

## 5. Running the Simulation

The Python virtual environment containing QNE-ADK, NetQASM, SquidASM and NetSquid must first be activated.

The experiment can then be run from the `Quantum_Network` folder using

```bash
qne experiment run my_exp
```

The results can be displayed using

```bash
qne experiment results my_exp
```

The experiment name `my_exp` can be replaced by the name assigned to the corresponding experiment.

## 6. Skills Learned

- Creation of an EPR pair between two quantum network nodes.
- Entanglement distribution between Alice and Bob.
- The use of `EPRSocket` for quantum network communication.
- The use of `NetQASMConnection` to connect an application to the backend.
- The difference between `create_keep()` and `recv_keep()`.
- Qubit measurements in the computational basis.
- Probabilistic individual results and correlated joint results.
- Quantum network simulations using NetQASM, SquidASM and NetSquid.
- Python functions and code organisation for two-node quantum applications.

## 7. Course

This project was completed as part of the *Quantum Computer and Quantum Internet Applications: Hands-on Training with QuTech's Quantum Demonstrators* course and my Personal Quantum Lab.

## 8. References

- [Quantum Network Explorer](https://www.quantum-network.com/)
- [NetQASM](https://github.com/QuTech-Delft/netqasm)
- [SquidASM](https://github.com/QuTech-Delft/squidasm)
- [NetSquid](https://netsquid.org/)
