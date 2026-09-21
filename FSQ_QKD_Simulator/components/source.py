# Import necessary packages
import numpy as np


# Generate photon numbers using Poisson distribution
def generate_photon_numbers(number_of_signals, mean_photon_number):
    if mean_photon_number > 0:
           photon_numbers = np.random.poisson(mean_photon_number, size=number_of_signals)
    else:
        raise ValueError("Error: The mean photon number cannot be smaller or equal to 0.")

    return (photon_numbers)


# Classify pulses
def classify_pulses(photon_numbers):
    # Initialization
    vacuum_count = 0
    single_photon_count = 0
    multiphoton_count = 0

    for photon_number in photon_numbers:
        if photon_number == 0:
            vacuum_count = vacuum_count + 1
        elif photon_number == 1:
            single_photon_count = single_photon_count + 1
        elif photon_number >= 2:
            multiphoton_count = multiphoton_count + 1

    return (vacuum_count, single_photon_count, multiphoton_count)


# Calculate count percentages
def calculate_pulse_percentages(number_of_signals, vacuum_count, single_photon_count, multiphoton_count):
    vacuum_percentage = vacuum_count / number_of_signals * 100
    single_photon_percentage = single_photon_count / number_of_signals * 100
    multiphoton_percentage = multiphoton_count / number_of_signals * 100

    return (vacuum_percentage, single_photon_percentage, multiphoton_percentage)