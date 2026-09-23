# Import necessary package
import math as m


# Calculate the communication rates, since FSO system evaluates in bits per second
def calculate_protocol_rates(number_of_signals, pulse_repetition_rate, detected_count, sifted_count, remaining_count):
    # Validate non-zero number of signals and pulse repition rate
    if number_of_signals <= 0:
        raise ValueError("Error. No signals transmitted.")
    
    if pulse_repetition_rate <= 0:
        raise ValueError("Error. No pulse repetition detected.")
   
    # Validate non-negative counts
    if detected_count < 0 or sifted_count < 0 or remaining_count < 0:
        raise ValueError("Error. Protocol counts cannot be negative.")

    # Calculate transmission duration, detection rate, sifted key rate and remaining key rate
    transmission_duration = number_of_signals/pulse_repetition_rate
    detection_rate = detected_count/transmission_duration
    sifted_key_rate = sifted_count/transmission_duration
    remaining_key_rate = remaining_count/transmission_duration

    return (transmission_duration, detection_rate, sifted_key_rate, remaining_key_rate)


# Calculate uncertainty in QBER using the binary Shannon entropy function
def binary_entropy(probability):
    # Validate realistic probability
    if probability < 0 or probability > 1:
        raise ValueError("Error. The probability has to be between 0 and 1 included.")

    # Conditions because of undefined value log2(0)
    if probability == 0 or probability == 1:
        return (0)

    # Calculate the binary entropy
    binary_entropy = -probability*m.log2(probability)-(1-probability)*m.log2(1-probability)

    return (binary_entropy)


# Calculate the secret fraction 
def calculate_secret_fraction(qber, error_correction_efficiency):
    # Validate QBER and Error Correction Efficiency
    if qber < 0 or qber > 1:
        raise ValueError("Error. QBER cannot be below 0 or above 1.")
    
    if error_correction_efficiency < 1:
        raise ValueError("Error-correction efficiency must be at least 1.")

    # Calculate binary Shannon entropy / Privacy Amplification Cost
    entropy = binary_entropy(qber)

    # Calculate secret fraction using the formula: r = 1 - estimated error-correction leakage - estimated privacy amplification cost
    secret_fraction = max(0, 1 - error_correction_efficiency*entropy - entropy)

    return (secret_fraction)


# Calculate secure key rate
def calculate_secure_key_rate(remaining_key_rate, secret_fraction, protocol_aborted):
    # Validate the remaining key rate and secret fraction
    if remaining_key_rate < 0:
        raise ValueError("Error. The remaining key rate cannot be below 0.")

    if secret_fraction < 0 or secret_fraction > 1:
        raise ValueError("Error. The secret fraction cannot be below 0 and above 1.")

    # Calculate secure key rate and choose to abort
    if protocol_aborted:
        secure_key_rate = 0
    else:
        secure_key_rate = remaining_key_rate * secret_fraction
    
    return secure_key_rate