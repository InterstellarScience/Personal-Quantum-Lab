# Import necessary packages
import numpy as np


# Create the channel loss count
def apply_channel_loss(photon_numbers, channel_transmittance):
    # Validate if transmittance is between 0 and 1
    if channel_transmittance < 0 or channel_transmittance > 1:
        raise ValueError("Error. Transmittance has to be in between 0 and 1.")

    # Generate the number of photons surviving the channel
    received_photon_numbers = np.random.binomial(photon_numbers, channel_transmittance)

    return (received_photon_numbers)