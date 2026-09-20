# Import necessary packages
import numpy as np


# Create the quantum bit error rate (QBER) calculator
def calculate_qber(alice_sifted_key, bob_sifted_key):
    counter = 0

    for i in range(len(alice_sifted_key)):
        if alice_sifted_key[i] != bob_sifted_key[i]:
            counter = counter + 1

    qber = counter / len(alice_sifted_key)

    return (qber)


# Create the QBER estimation by public sampling
def select_test_bits(alice_sifted_key, bob_sifted_key, test_fraction):
    if len(alice_sifted_key) == 0:
        raise ValueError("Cannot select test bits from an empty sifted key.")

    number_of_test_bits = max(1, int(test_fraction * len(alice_sifted_key)))

    random_select = np.random.choice(len(alice_sifted_key), size=number_of_test_bits, replace=False)

    alice_test_bits = []
    bob_test_bits = []

    for i in random_select:
        alice_test_bits.append(int(alice_sifted_key[i]))
        bob_test_bits.append(int(bob_sifted_key[i]))

    alice_remaining_key = []
    bob_remaining_key = []

    for i in range(len(alice_sifted_key)):
        if i not in random_select:
            alice_remaining_key.append(int(alice_sifted_key[i]))
            bob_remaining_key.append(int(bob_sifted_key[i]))

    return (random_select, alice_test_bits, bob_test_bits, alice_remaining_key, bob_remaining_key)


# Abort transmission if QBER > 11%
def should_abort(estimated_qber, qber_threshold):
    return estimated_qber > qber_threshold