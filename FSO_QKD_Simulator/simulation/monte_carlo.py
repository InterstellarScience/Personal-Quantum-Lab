# Import necessary packages
from protocols.bb84 import (prepare_single_qubit, measure_single_qubit_bob, simulate_single_qubit)
from attacks.intercept_resend import(intercept_single_qubit)
import numpy as np


# Simulator for the real qiskit circuit (slow)
# Create the simulation for every single transmissible qubit
def run_transmissions(alice_bits, alice_bases, bob_bases, eve_intercepts, eve_bases, detected_photon_numbers, dark_count_flags, misalignment_flags, background_count_flags):
    bob_bits = []

    for i in range(len(alice_bits)):
        # Checking if pulses arrived at Bob's station
        if detected_photon_numbers[i] == 0:
            if dark_count_flags[i] or background_count_flags[i]:
                bob_bits.append(np.random.randint(0, 2))
            else:
                bob_bits.append(None)

            continue

        # Continue with non-vacuum logic
        qc = prepare_single_qubit(alice_bits[i], alice_bases[i])
        qc = intercept_single_qubit(qc, eve_intercepts[i], eve_bases[i])
        qc = measure_single_qubit_bob(qc, bob_bases[i])
        
        # Check for misalignment of encoding and measurement bases
        bob_bit = simulate_single_qubit(qc)

        if misalignment_flags[i]:
            bob_bit = 1 - bob_bit 

        # Append to list
        bob_bits.append(bob_bit)

    return (bob_bits)


## Create a fast simulator for FSO implementation
# Translate quantum measruement into classical probability
def measure_bit(prepared_bit, prepared_basis, measurement_basis):
    if prepared_basis == measurement_basis:
        return (prepared_bit)
    else:
        return (np.random.randint(0,2))

# Create the fast simulation
def run_transmissions_fast(alice_bits, alice_bases, bob_bases, eve_intercepts, eve_bases, detected_photon_numbers, dark_count_flags, misalignment_flags, background_count_flags):
    bob_bits = []

    for i in range(len(alice_bits)):
        # Checking if pulses arrived at Bob's station
        if detected_photon_numbers[i] == 0:
            if dark_count_flags[i] or background_count_flags[i]:
                bob_bits.append(np.random.randint(0, 2))
            else:
                bob_bits.append(None)
        
            continue

        # Only non-vacuum pulses
        if eve_intercepts[i]:
            eve_bit = measure_bit(alice_bits[i], alice_bases[i], eve_bases[i])
            bob_bit = measure_bit(eve_bit, eve_bases[i],  bob_bases[i])
        else:
            # Measure qubit
            bob_bit = measure_bit(alice_bits[i], alice_bases[i], bob_bases[i])

        # Check for misalignment of encoding and measurement bases
        if misalignment_flags[i]:
            bob_bit = 1 - bob_bit

        bob_bits.append(bob_bit)

    return (bob_bits)