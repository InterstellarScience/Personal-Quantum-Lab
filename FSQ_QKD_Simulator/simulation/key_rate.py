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