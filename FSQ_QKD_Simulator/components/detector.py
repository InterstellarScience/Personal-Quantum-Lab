# Import necessary packages
import numpy as np

# Create detector efficienty
def apply_detector_efficiency(received_photon_numbers, detector_efficiency):
    # Validate if detector efficiency is between 0 and 1
    if detector_efficiency < 0 or detector_efficiency > 1:
        raise ValueError("Error. Detector efficiency has to be in between 0 and 1.")

    # Generate the detected number of photons
    detected_photon_numbers = np.random.binomial(received_photon_numbers, detector_efficiency)

    return (detected_photon_numbers)


# Create dark count probability: the probability of a false detector click during one singal window
def  generate_dark_counts(detected_photon_numbers, dark_count_probability):
    # Validate probability
    if dark_count_probability < 0 or dark_count_probability > 1:
        raise ValueError("Error. Dark count probability cannot be under 0 or over 1.")
    
    dark_count_flags = []

    # Add the dark counts
    for detected_count in detected_photon_numbers:
        if detected_count > 0:
            dark_count_flags.append(False)
        elif detected_count == 0:
            random_decimal = np.random.random()
            dark_count_flags.append(random_decimal < dark_count_probability)
            
    return (dark_count_flags)


# Create possible misalignment of Alice's and Bob's optical encoding and measurment bases
def generate_misalignment_flags(detected_photon_numbers, misalignment_probability):
    # Validate probability
    if misalignment_probability < 0 or misalignment_probability > 1:
        raise ValueError("Error. Misalignment probability cannot be under 0 or over 1.")

    misalignment_flags = []

    # Add the misalignment count
    for detected_photons in detected_photon_numbers:
        if detected_photons == 0:
            misalignment_flags.append(False)
        elif detected_photons > 0:
            random_decimal = np.random.random()
            misalignment_flags.append(random_decimal < misalignment_probability)

    return (misalignment_flags)


# Account for possible background noise detected
def generate_background_counts(detected_photon_numbers, mean_background_photons):

    background_noise = []

    # Check whether background noise was found
    if mean_background_photons <0:
        raise ValueError("Mean background photon number cannot be negative.")

    # Add the background noise counts
    for detected_photons in detected_photon_numbers:
        if detected_photons > 0:
            background_noise.append(False)
        else:
            background_count = np.random.poisson(mean_background_photons)
            background_noise.append(background_count > 0)

    return (background_noise)
