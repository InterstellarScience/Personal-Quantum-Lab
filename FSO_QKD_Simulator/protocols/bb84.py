# Import necessary packages
import numpy as np
import qiskit as qk
import qiskit_aer as aer


# Create random bits generator for Alice's bit chain
def generate_random_bits(number_of_bits):
    list_of_bits = []

    for i in range(number_of_bits):
        random_bit = np.random.randint(0,2)
        list_of_bits.append(random_bit)

    return(list_of_bits)


# Create function that prepares each qubit using the bases list of Alice
def prepare_qubits(bits, bases):
    qc = qk.QuantumCircuit(len(bits), len(bases)) # Create the quantum circuit

    # 'Convert' classical bits to quantum bits
    for i in range(len(bits)):
        #Z-basis check
        if bits[i] == 0 and bases[i] == 0:
            qc.id(i)

        if bits[i] == 1 and bases[i] == 0:
            qc.x(i)

        #X-basis check
        if bits[i] == 0 and bases[i] == 1:
            qc.h(i)

        if bits[i] == 1 and bases[i] == 1:
            qc.h(i)
            qc.z(i)

    return (qc)


# Measure the qubits with Bob
def measure_qubits(qc, bases):
    for i in range(len(bases)):
        if bases[i] == 0:
            qc.measure(i,i)

        else:
            qc.h(i)
            qc.measure(i,i)

    return (qc)


# Create quantum circuit simulator
def qc_simulator(qc):
    # Simulate
    circuit_simul = aer.AerSimulator()
    compiled_qc = qk.transpile(qc, circuit_simul)
    job = circuit_simul.run(compiled_qc, shots=1)
    result = job.result()
    counts = result.get_counts(compiled_qc)
    print("Bob's measurement gives: ", counts)

    # Convert the dictionary into a usable list
    convert = list(counts.keys())[0]
    convert = convert[::-1] # Since Qiskit returns the bits in opposite direction from the used index order  

    # Create Bob's list of bits
    bob_bits = []

    for i in convert:
        bob_bits.append(int(i))

    print("Bob's list of bits is : ", bob_bits)

    return (bob_bits)


# Create the sift keys
def sift_keys(a_bits, a_bases, b_bits, b_bases, verbose = True):
    # Create empty list for matching indices 
    matching_indices = []

    for i in range(len(a_bits)):
        if a_bases[i] == b_bases[i] and b_bits[i] is not None:
            matching_indices.append(i)

    # Create sift keys for Alice and Bob
    alice_sifted_key = []
    bob_sifted_key = []

    for i in matching_indices:
        alice_sifted_key.append(int(a_bits[i]))
        bob_sifted_key.append(int(b_bits[i]))

    # Verify if both sifted keys are the same
    if verbose:
        if alice_sifted_key == bob_sifted_key:
            print("Success: Alice and Bob's sifted keys match.")
        else:
            print("Caution: Alice and Bob's sifted keys don't match. Channel disturbance may be present.")

    return (matching_indices, alice_sifted_key, bob_sifted_key)


## Create simulator for N-transmissible signals
# Create quantum circuit for single qubit
def prepare_single_qubit(bit, basis):
    # Create quantum circuit
    qc = qk.QuantumCircuit(1,1)

    #Z-basis check
    if bit == 0 and basis == 0:
        qc.id(0)
    
    if bit == 1 and basis == 0:
        qc.x(0)
    
    #X-basis check
    if bit == 0 and basis == 1:
        qc.h(0)
    
    if bit == 1 and basis == 1:
        qc.h(0)
        qc.z(0)

    return (qc)


# Create Bob's single qubit measurement function
def measure_single_qubit_bob(qc, bob_basis):
    if bob_basis == 0:
        qc.measure(0,0)

    else:
        qc.h(0)
        qc.measure(0,0)

    return (qc)


# Simulate single qubit
def simulate_single_qubit(qc):
    # Simulate
    circuit_simul = aer.AerSimulator()
    compiled_qc = qk.transpile(qc, circuit_simul)
    job = circuit_simul.run(compiled_qc, shots=1)
    result = job.result()
    counts = result.get_counts(compiled_qc)

    # Convert the dictionary into a usable list
    convert = list(counts.keys())[0]

    # Create Bob's bit
    bob_bit = int(convert[0])

    return (bob_bit)