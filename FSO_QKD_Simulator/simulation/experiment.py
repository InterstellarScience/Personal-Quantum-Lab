# Import necessary packages
from protocols.bb84 import (generate_random_bits, sift_keys)
from attacks.intercept_resend import (generate_eve_choices)
from post_processing.qber import (calculate_qber, select_test_bits, should_abort)
from simulation.monte_carlo import (run_transmissions, run_transmissions_fast)
from components.source import (generate_photon_numbers, classify_pulses, calculate_pulse_percentages)
from fs_channel.free_space import(apply_channel_loss, calculate_beam_radius, calculate_geometric_transmittance, calculate_atmospheric_transmittance)
from components.detector import (apply_detector_efficiency, generate_dark_counts, generate_misalignment_flags, generate_background_counts)
from simulation.key_rate import(calculate_protocol_rates, calculate_secret_fraction, calculate_secure_key_rate)


# Run the simulation using the config.py file
def run_simulation(config):
    number_of_signals = config["number_of_signals"]
    interception_probability = config["eve_interception_probability"]
    mean_photon_number = config["mean_photon_number"]
    distance = config["distance"]
    wavelength = config["wavelength_nm"] * 1e-9
    beam_waist = config["beam_waist"]
    receiver_aperture_diameter = config["receiver_aperture_diameter"]
    attenuation = config["attenuation_db_per_km"]
    detector_efficiency = config["detector_efficiency"]
    dark_count_probability = config["dark_count_probability"]
    mean_background_photons = config["mean_background_photons"]
    misalignment_probability = config["misalignment_probability"]
    test_fraction = config["test_fraction"]
    pulse_repetition_rate = config["pulse_repetition_rate"]
    error_correction_efficiency = config["error_correction_efficiency"]
    qber_threshold = config["qber_threshold"]
    simulation_mode = config["simulation_mode"].strip().lower()
    verbose = config.get("verbose", False)

    ## For faster, smoother output
    def log(*args, **kwargs):  
        if verbose:
            print(*args, **kwargs)


    ## Validate initial values such as number of signals and Eve's interception probability
    # Realistic number of signals value check
    if number_of_signals <= 0:
        raise ValueError("The number of signals must be greater than zero.")

    # Create condition in case the probability is < 0 or > 1 
    if interception_probability < 0 or interception_probability > 1:  
        raise ValueError("Eve's interception probability must be between 0 and 1 included.")

    ## Create the bits and bases of Alice and Bob and create the quantum circuit
    alice_bits = generate_random_bits(number_of_signals)
    alice_bases = generate_random_bits(number_of_signals)
    bob_bases = generate_random_bits(number_of_signals)


    ## Create the FSO setup
    # Generate photon numbers
    photon_numbers = generate_photon_numbers(len(alice_bits), mean_photon_number)

    # Pre-send: Classify photon numbers
    vacuum_count, single_photon_count, multiphoton_count = classify_pulses(photon_numbers)
    vacuum_percentage, single_photon_percentage, multiphoton_percentage = calculate_pulse_percentages(len(alice_bits), vacuum_count, single_photon_count, multiphoton_count)
    log(f"Pre-send: Vacuum pulses: {vacuum_count} - {vacuum_percentage:.2f}%")
    log(f"Pre-send: Single photon pulses: {single_photon_count} - {single_photon_percentage:.2f}%")
    log(f"Pre-send: Multiphoton pulses: {multiphoton_count} - {multiphoton_percentage:.2f}%")


    ## Calculate Gaussian beam propagation
    # Calculate beam radius
    beam_radius = calculate_beam_radius(distance, wavelength, beam_waist)
    log(f"Beam radius at Bob: {beam_radius:.6f} m")

    # Calculate geometric transmittance
    receiver_aperture_radius = receiver_aperture_diameter / 2
    geometric_transmittance = calculate_geometric_transmittance(beam_radius, receiver_aperture_radius)
    log(f"Geometric transmittance: {geometric_transmittance:.4f}")

    # Calculate atmospheric transmittance
    atmospheric_transmittance = calculate_atmospheric_transmittance(distance, attenuation)
    log(f"Atmospheric transmittance: {atmospheric_transmittance:.4f}")

    # Give channel transmittance variable and apply channel loss
    channel_transmittance = geometric_transmittance * atmospheric_transmittance
    log(f"Total channel transmittance: {channel_transmittance:.4f}")
    received_photon_numbers = apply_channel_loss(photon_numbers, channel_transmittance)


    ## Post-send: Classify photon numbers
    received_vacuum_count, received_single_photon_count, received_multiphoton_count = classify_pulses(received_photon_numbers)
    received_vacuum_percentage, received_single_photon_percentage, received_multiphoton_percentage = calculate_pulse_percentages(len(alice_bits), received_vacuum_count, received_single_photon_count, received_multiphoton_count)
    log(f"Zero received vacuum pulses: {received_vacuum_count} - {received_vacuum_percentage:.2f}%")
    log(f"Received single photon pulses: {received_single_photon_count} - {received_single_photon_percentage:.2f}%")
    log(f"Received multiphoton pulses: {received_multiphoton_count} - {received_multiphoton_percentage:.2f}%")

    # Give a detector efficiency
    detected_photon_numbers = apply_detector_efficiency(received_photon_numbers, detector_efficiency)

    # Post-send: Classify detected photon numbers
    detected_vacuum_count, detected_single_photon_count, detected_multiphoton_count = classify_pulses(detected_photon_numbers)
    detected_vacuum_percentage, detected_single_photon_percentage, detected_multiphoton_percentage = calculate_pulse_percentages(len(alice_bits), detected_vacuum_count, detected_single_photon_count, detected_multiphoton_count)
    log(f"Zero detected vacuum pulses: {detected_vacuum_count} - {detected_vacuum_percentage:.2f}%")
    log(f"Detected single photon pulses: {detected_single_photon_count} - {detected_single_photon_percentage:.2f}%")
    log(f"Detected multiphoton pulses: {detected_multiphoton_count} - {detected_multiphoton_percentage:.2f}%")

    # Generate dark count probabilities and apply them if necessary
    dark_count_flags = generate_dark_counts(detected_photon_numbers, dark_count_probability)
    log("Dark-count detections:", sum(dark_count_flags))

    # Generate misalignment probability of Alice's and Bob's encoding & measurement bases
    misalignment_flags = generate_misalignment_flags(detected_photon_numbers, misalignment_probability)

    # Generate the possible background noise counts
    background_count_flags = generate_background_counts(detected_photon_numbers, mean_background_photons)
    log("Background noise detected: ", sum(background_count_flags), " counts.")


    ## Interception procedure from Eve
    # Create the interception decision for Eve
    eve_intercepts, eve_bases = generate_eve_choices(number_of_signals, interception_probability)


    ## Choose simulation mode (fast by default)
    if simulation_mode == "qiskit":
        bob_bits = run_transmissions(alice_bits, alice_bases, bob_bases, eve_intercepts, eve_bases, detected_photon_numbers, dark_count_flags, misalignment_flags, background_count_flags)
    elif simulation_mode == "fast":
        bob_bits = run_transmissions_fast(alice_bits, alice_bases, bob_bases, eve_intercepts, eve_bases, detected_photon_numbers, dark_count_flags, misalignment_flags, background_count_flags)
    else:
        raise ValueError("Incorrect choice. Re-try the experiment.")
    

    ## Get the matching indices and sifted keys of Alice and Bob
    matching_indices, alice_sifted_key, bob_sifted_key = sift_keys(alice_bits, alice_bases, bob_bits, bob_bases, verbose=verbose)
    log("Detected signals:", sum(bit is not None for bit in bob_bits))
    log("Sifted-key length:", len(alice_sifted_key))


    ## Post-processing
    # Get the QBER %
    qber = calculate_qber(alice_sifted_key, bob_sifted_key)
    log("QBER:", qber)
    log("QBER percentage:", qber * 100, "%")

    # Get the QBER estimation public sampling
    if test_fraction <= 0 or test_fraction >= 1:
        raise ValueError("The test fraction must be greater than 0 and smaller than 1.")
    random_select, alice_test_bits, bob_test_bits, alice_remaining_key, bob_remaining_key = select_test_bits(alice_sifted_key, bob_sifted_key, test_fraction)
    estimated_qber = calculate_qber(alice_test_bits, bob_test_bits)
    log("The estimated QBER is: " , estimated_qber * 100, "%.")

    # Calculate protocol rates
    # Parameters
    detected_counts = sum(bit is not None for bit in bob_bits)
    sifted_count = len(alice_sifted_key)
    remaining_count = len(alice_remaining_key)

    # The calculation and results
    transmission_duration , detection_rate, sifted_key_rate, remaining_key_rate = calculate_protocol_rates(len(alice_bits), pulse_repetition_rate, detected_counts, sifted_count, remaining_count)
    log(f"Transmission duration: {transmission_duration:.6f} s")
    log(f"Detection rate: {detection_rate:.2f} detections/s")
    log(f"Sifted key rate: {sifted_key_rate:.2f} bits/s")
    log(f"Remaining key rate: {remaining_key_rate:.2f} bits/s")

    # Continue or abort transmission
    decision = should_abort(estimated_qber,qber_threshold)

    # Calculate secret fraction and secure key rate
    secret_fraction = calculate_secret_fraction(estimated_qber, error_correction_efficiency)
    secure_key_rate = calculate_secure_key_rate(remaining_key_rate, secret_fraction, decision)
    log(f"Secret fraction: {secret_fraction:.4f}")
    log(f"Secure key rate: {secure_key_rate:.2f} bits/s")

    # Decision
    if decision:
        log("Protocol aborted: the estimated QBER exceeds the security threshold.")
    elif secret_fraction == 0:
        log("No secure key can be extracted with the selected error-correction efficiency.")
    else:
        log("QBER test passed: a positive secure key rate can be extracted.")

    return{
    "qber": qber,
    "estimated_qber": estimated_qber,
    "detected_count": detected_counts,
    "sifted_count": sifted_count,
    "remaining_count": remaining_count,
    "detection_rate": detection_rate,
    "sifted_key_rate": sifted_key_rate,
    "remaining_key_rate": remaining_key_rate,
    "secret_fraction": secret_fraction,
    "secure_key_rate": secure_key_rate,
    "protocol_aborted": decision,
    "channel_transmittance": channel_transmittance}