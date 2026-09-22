# Import necessary packages
import numpy as np
import math as m


# Create the channel loss count
def apply_channel_loss(photon_numbers, channel_transmittance):
    # Validate if transmittance is between 0 and 1
    if channel_transmittance < 0 or channel_transmittance > 1:
        raise ValueError("Error. Transmittance has to be in between 0 and 1.")

    # Generate the number of photons surviving the channel
    received_photon_numbers = np.random.binomial(photon_numbers, channel_transmittance)

    return (received_photon_numbers)


# Create channel transmittance with Gaussian-beam physics
def calculate_beam_radius(distance, wavelength, beam_waist):
    # Validate distance z
    if distance < 0:
        raise ValueError("Error. Distance cannot be negative.")

    # Validate wavelength lambda
    if wavelength <= 0:
        raise ValueError("Error. Wavelength cannot be smaller or equal to 0.")

    # Validate beam waist w_0
    if beam_waist <= 0:
        raise ValueError("Error. Beam waist cannot be smaller or equal to 0.")

    # Calulate Rayleigh range
    z_R = (m.pi*beam_waist**2)/wavelength

    # Calulcate beam radius
    beam_radius = beam_waist*m.sqrt(1+(distance/z_R)**2)

    return (beam_radius)


# Calculate the geometric transmittance, which is the fraction of the Gaussian beam captured by Bob's circular receiver aperture
def calculate_geometric_transmittance(beam_radius, receiver_aperture_radius):
    # Validate beam radius and receiver aperture radius
    if beam_radius <=0:
        raise ValueError("Error. Beam radius cannot be smaller or equal to 0.")

    if receiver_aperture_radius <=0:
        raise ValueError("Error. Receiver aperture radius cannot be smaller or equal to 0.")
 
    # Calculate geometric transmittance
    geometric_transmittance = 1 - m.exp(- 2*(receiver_aperture_radius/beam_radius)**2)

    return (geometric_transmittance)
