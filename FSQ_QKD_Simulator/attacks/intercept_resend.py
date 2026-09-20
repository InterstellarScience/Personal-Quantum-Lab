# Import the necessary package
import numpy as np


# Create Eve's choices generator
def generate_eve_choices(number_of_signals, interception_probability):
    # Create the decision for Eve to intercept
    eve_intercepts = []

    for i in range(number_of_signals):
        random_decimal = np.random.random()
        decision = random_decimal < interception_probability
        eve_intercepts.append(decision)

    # Create Eve's bases
    eve_bases = []

    for i in range(number_of_signals):
        random_bit = np.random.randint(0,2)
        eve_bases.append(random_bit)
    
    return (eve_intercepts, eve_bases)


# Create the interception and resend to Bob function
def intercept_and_resend(qc, eve_intercepts, eve_bases):

    for i in range(len(eve_intercepts)):
        if eve_intercepts[i]:
            if eve_bases[i] == 0:
                qc.measure(i,i)

            else:
                qc.h(i)
                qc.measure(i,i)
                qc.h(i)

    return(qc)