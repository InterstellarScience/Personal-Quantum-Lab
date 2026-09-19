## Import necessary packages
from protocols.bb84 import (generate_random_bits, prepare_qubits, measure_qubits, qc_simulator, sift_keys)
from attacks.intercept_resend import(generate_eve_choices, intercept_and_resend)


## Prepare Alice's qubits
# Create the input for Alice's number of bits
n = int(input("Give the number of bits Alice wants to send to Bob: "))

# Create condition in case no bit is given or if > 25 (limit the current multi-qubit statevector simulation to avoid excessive memory use)
if n <= 0:
    raise ValueError("The number of bits must be greater than 0.")
if n > 25:
    raise ValueError("The number of bits must be smaller than 26.")


## Prepare the intercept probability of Eve
# Create intercept probability of Eve intercepting information of the transmission
intercept_probability = float(input("Give Eve's interception probability between 0 and 1: "))

# Create condition in case the probability is < 0 or > 1 
if intercept_probability < 0 or intercept_probability > 1:
    raise ValueError("Eve's interception probability must be between 0 and 1 included.")


## Run the bits and bases generator of Alice and create the quantum circuit
# Run the random generator
alice_bits = generate_random_bits(n)
print("Alice's list of bits is: ", alice_bits)

# Create Alice's bases
alice_bases = generate_random_bits(n)
print("Alice's list of bases is: ", alice_bases)

# Run the quantum circuit
qc = prepare_qubits(alice_bits, alice_bases)


## Interception procedure from Eve
# Create the interception decision for Eve
eve_intercepts, eve_bases = generate_eve_choices(n, intercept_probability)
print("Eve's interception decisions: ", eve_intercepts)
print("Eve's bases: ", eve_bases)

# Intercept and resend by Eve
qc = intercept_and_resend(qc, eve_intercepts, eve_bases)


## Create Bob's bases and measurement procedure
# Create Bob's bases
bob_bases = generate_random_bits(n)
print("Bob's list of bases is: ", bob_bases)

# Run Bob's measurement process
qc = measure_qubits(qc, bob_bases)

# Run the simulation to get Bob's list of bits
bob_bits = qc_simulator(qc)

# Get the matching indices and sifted keys of Alice and Bob
matching_indices, alice_sifted_key, bob_sifted_key = sift_keys(alice_bits, alice_bases, bob_bits, bob_bases)