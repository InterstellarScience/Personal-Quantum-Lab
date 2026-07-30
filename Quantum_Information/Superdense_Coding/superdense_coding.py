import qiskit as qk
import qiskit_aer as aer
import matplotlib.pyplot as plt
from pathlib import Path

# Prepare for saving the results into the images folder
project_folder = Path(__file__).resolve().parent
images_folder = project_folder / "images"
images_folder.mkdir(exist_ok=True)

# Alice has two classical bits c0 and c1
# Alice has a half of a Bell pair
# Bob has the other half of the Bell pair
# Alice can choose which Bell state she sends to Bob
# Bob needs to figure out the Bell state to measure c0 and c1

# Construct the quantum circuit
qc = qk.QuantumCircuit(2,2)


# Create 2 classical bits, input either 0 and/or 1
c0 = int(input("Choose your first classical bit 0 or 1: "))
c1 = int(input("Choose your second classical bit 0 or 1: "))


# Creating the initial Bell state
def create_bell_state(qc):
    qc.h(0)
    qc.cx(0,1)


# Alice chooses a two-bit classical message and encodes it into the shared Bell state
def encode_message(qc, c0, c1):
    if c0 == 0 and c1 == 0:
        qc.id(0)
    elif c0 == 1 and c1 == 0:
        qc.x(0)
    elif c0 == 0 and c1 == 1:
        qc.z(0)
    elif c0 == 1 and c1 == 1:
        qc.x(0)
        qc.z(0)
    else:
        raise ValueError("Unknown classical bit value.")


# Bob decodes the message
def decode_message(qc):
    qc.cx(0,1)
    qc.h(0)
    qc.measure(0,0)
    qc.measure(1,1)


# Run simulation to verify the qc -> classical bits are displayed as c0c1
def superdense_coding_simulation(qc):
    circuit_simul = aer.AerSimulator()
    job = circuit_simul.run(qc, shots=1024)
    result = job.result()
    counts = result.get_counts()
    print(counts)


# Run the program
create_bell_state(qc)
encode_message(qc, c0, c1)
decode_message(qc)

# Draw the circuit and and print the classical bits
print(qc.draw())
print(f"Alice's message: {c0}{c1}")

# Printing and saving the circuit
fig = qc.draw(output="mpl")
fig.savefig(images_folder / "superdense_coding_circuit.png")
plt.show()

# Run the simulation
superdense_coding_simulation(qc)