## Import necessary packages
from protocols.bb84 import (generate_random_bits, sift_keys)
from attacks.intercept_resend import (generate_eve_choices)
from post_processing.qber import (calculate_qber, select_test_bits, should_abort)
from simulation.monte_carlo import (run_transmissions, run_transmissions_fast)
from components.source import (generate_photon_numbers, classify_pulses, calculate_pulse_percentages)
from fs_channel.free_space import(apply_channel_loss, calculate_beam_radius, calculate_geometric_transmittance, calculate_atmospheric_transmittance)
from components.detector import (apply_detector_efficiency, generate_dark_counts, generate_misalignment_flags, generate_background_counts)
from simulation.key_rate import(calculate_protocol_rates, calculate_secret_fraction, calculate_secure_key_rate)


## Prepare Alice's qubits
# Create the input for Alice's number of signals
n = int(input("Give the number of signals Alice wants to send to Bob: "))

# Realistic n value check
if n <= 0:
    raise ValueError("The number of signals must be greater than zero.")


## Prepare the intercept probability of Eve
# Create intercept probability of Eve intercepting information of the transmission
intercept_probability = float(input("Give Eve's interception probability between 0 and 1: "))

# Create condition in case the probability is < 0 or > 1 
if intercept_probability < 0 or intercept_probability > 1:
    raise ValueError("Eve's interception probability must be between 0 and 1 included.")


## Run the bits and bases generator of Alice and create the quantum circuit
# Run the random generator
alice_bits = generate_random_bits(n)

# Create Alice's bases
alice_bases = generate_random_bits(n)

# Create Bob's bases
bob_bases = generate_random_bits(n)


## Create the FSO setup
# Generate photon numbers
mean_photon_number = float(input("Enter the source's mean photon number mu: "))
photon_numbers = generate_photon_numbers(len(alice_bits), mean_photon_number)

# Pre-send: Classify photon numbers
vacuum_count, single_photon_count, multiphoton_count = classify_pulses(photon_numbers)
vacuum_percentage, single_photon_percentage, multiphoton_percentage = calculate_pulse_percentages(len(alice_bits), vacuum_count, single_photon_count, multiphoton_count)
print(f"Pre-send: Vacuum pulses: {vacuum_count} - {vacuum_percentage:.2f}%")
print(f"Pre-send: Single photon pulses: {single_photon_count} - {single_photon_percentage:.2f}%")
print(f"Pre-send: Multiphoton pulses: {multiphoton_count} - {multiphoton_percentage:.2f}%")


## Calculate Gaussian beam propagation
# Calculate beam radius
distance = float(input("Enter propagation distance in metres: "))
wavelength_nm = float(input("Enter wavelength in nanometres: "))
beam_waist = float(input("Enter transmitter beam waist in metres: "))
wavelength = wavelength_nm * 1e-9
beam_radius = calculate_beam_radius(distance, wavelength, beam_waist)
print(f"Beam radius at Bob: {beam_radius:.6f} m")

# Calculate geometric transmittance
receiver_aperture_diameter = float(input("Enter Bob's receiver aperture diameter in metres: "))
receiver_aperture_radius = receiver_aperture_diameter / 2
geometric_transmittance = calculate_geometric_transmittance(beam_radius, receiver_aperture_radius)
print(f"Geometric transmittance: {geometric_transmittance:.4f}")

# Calculate atmospheric transmittance
attenuation = float(input("Enter the atmospheric attenuation: "))
atmospheric_transmittance = calculate_atmospheric_transmittance(distance, attenuation)
print(f"Atmospheric transmittance: {atmospheric_transmittance:.4f}")

# Give channel transmittance variable and apply channel loss
channel_transmittance = geometric_transmittance * atmospheric_transmittance
print(f"Total channel transmittance: {channel_transmittance:.4f}")
received_photon_numbers = apply_channel_loss(photon_numbers, channel_transmittance)


## Post-send: Classify photon numbers
received_vacuum_count, received_single_photon_count, received_multiphoton_count = classify_pulses(received_photon_numbers)
received_vacuum_percentage, received_single_photon_percentage, received_multiphoton_percentage = calculate_pulse_percentages(len(alice_bits), received_vacuum_count, received_single_photon_count, received_multiphoton_count)
print(f"Zero received vacuum pulses: {received_vacuum_count} - {received_vacuum_percentage:.2f}%")
print(f"Received single photon pulses: {received_single_photon_count} - {received_single_photon_percentage:.2f}%")
print(f"Received multiphoton pulses: {received_multiphoton_count} - {received_multiphoton_percentage:.2f}%")

# Give a detector efficiency
detector_efficiency = float(input("Enter the detector efficiency between 0 and 1: "))
detected_photon_numbers = apply_detector_efficiency(received_photon_numbers, detector_efficiency)

# Post-send: Classify detected photon numbers
detected_vacuum_count, detected_single_photon_count, detected_multiphoton_count = classify_pulses(detected_photon_numbers)
detected_vacuum_percentage, detected_single_photon_percentage, detected_multiphoton_percentage = calculate_pulse_percentages(len(alice_bits), detected_vacuum_count, detected_single_photon_count, detected_multiphoton_count)
print(f"Zero detected vacuum pulses: {detected_vacuum_count} - {detected_vacuum_percentage:.2f}%")
print(f"Detected single photon pulses: {detected_single_photon_count} - {detected_single_photon_percentage:.2f}%")
print(f"Detected multiphoton pulses: {detected_multiphoton_count} - {detected_multiphoton_percentage:.2f}%")

# Generate dark count probabilities and apply them if necessary
dark_count_probability = float(input("Enter the dark-count probability per signal window: "))
dark_count_flags = generate_dark_counts(detected_photon_numbers,dark_count_probability)
print("Dark-count detections:", sum(dark_count_flags))

# Generate misalignment probability of Alice's and Bob's encoding & measurement bases
misalignment_probability = float(input("Enter the misalignment probability between 0 and 1: "))
misalignment_flags = generate_misalignment_flags(detected_photon_numbers, misalignment_probability)

# Generate the possible background noise counts
mean_background_photons = float(input("Enter the mean background photons per signal window: "))
background_count_flags = generate_background_counts(detected_photon_numbers, mean_background_photons)
print("Background noise detected: ", sum(background_count_flags), " counts.")


## Interception procedure from Eve
# Create the interception decision for Eve
eve_intercepts, eve_bases = generate_eve_choices(n, intercept_probability)


## Create simulator for N-transmissible signals
# Give the choice to choose between detailed qiskit circuit simulations (N = 10'000 signals already takes some time, so choose wisely) or fast, large Monte Carlo simulations
simulation_mode = input("Choose simulation mode ('qiskit' or 'fast'): ").lower()
 
if simulation_mode == "qiskit":
    bob_bits = run_transmissions(alice_bits, alice_bases, bob_bases, eve_intercepts, eve_bases, detected_photon_numbers, dark_count_flags, misalignment_flags, background_count_flags)
elif simulation_mode == "fast":
    bob_bits = run_transmissions_fast(alice_bits, alice_bases, bob_bases, eve_intercepts, eve_bases, detected_photon_numbers, dark_count_flags, misalignment_flags, background_count_flags)
else:
    raise ValueError("Incorrect choice. Re-try the experiment.")


## Get the matching indices and sifted keys of Alice and Bob
matching_indices, alice_sifted_key, bob_sifted_key = sift_keys(alice_bits, alice_bases, bob_bits, bob_bases)
print("Detected signals:", sum(bit is not None for bit in bob_bits))
print("Sifted-key length:", len(alice_sifted_key))


## Post-processing
# Get the QBER %
qber = calculate_qber(alice_sifted_key, bob_sifted_key)
print("QBER:", qber)
print("QBER percentage:", qber * 100, "%")

# Get the QBER estimation public sampling
test_fraction = float(input("Input a fraction between 0 and 1 to calculate how many sifted positions are tested, with 0 and 1 being excluded: "))
if test_fraction <= 0 or test_fraction >= 1:
    raise ValueError("The test fraction must be greater than 0 and smaller than 1.")
random_select, alice_test_bits, bob_test_bits, alice_remaining_key, bob_remaining_key = select_test_bits(alice_sifted_key, bob_sifted_key, test_fraction)
estimated_qber = calculate_qber(alice_test_bits, bob_test_bits)
print("The estimated QBER is: " , estimated_qber * 100, "%.")

# Calculate protocol rates
# Parameters
pulse_repetition_rate = float(input("Enter the pulse repetition rate in Hz: "))
detected_counts = sum(bit is not None for bit in bob_bits)
sifted_count = len(alice_sifted_key)
remaining_count = len(alice_remaining_key)

# The calculation and results
transmission_duration , detection_rate, sifted_key_rate, remaining_key_rate = calculate_protocol_rates(len(alice_bits), pulse_repetition_rate, detected_counts, sifted_count, remaining_count)
print(f"Transmission duration: {transmission_duration:.6f} s")
print(f"Detection rate: {detection_rate:.2f} detections/s")
print(f"Sifted key rate: {sifted_key_rate:.2f} bits/s")
print(f"Remaining key rate: {remaining_key_rate:.2f} bits/s")

# Continue or abort transmission
qber_threshold = 0.11
decision = should_abort(estimated_qber,qber_threshold)

# Calculate secret fraction and secure key rate
error_correction_efficiency = float(input("Enter the error-correction efficiency (>= 1): "))
secret_fraction = calculate_secret_fraction(estimated_qber, error_correction_efficiency)
secure_key_rate = calculate_secure_key_rate(remaining_key_rate, secret_fraction, decision)
print(f"Secret fraction: {secret_fraction:.4f}")
print(f"Secure key rate: {secure_key_rate:.2f} bits/s")

# Decision
if decision:
    print("Protocol aborted: the estimated QBER exceeds the security threshold.")
elif secret_fraction == 0:
    print("No secure key can be extracted with the selected error-correction efficiency.")
else:
    print("QBER test passed: a positive secure key rate can be extracted.")
