import qiskit as qk
import qiskit_aer as aer
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# Prepare for saving the results into the images folder
project_folder = Path(__file__).resolve().parent
images_folder = project_folder / "images"
images_folder.mkdir(exist_ok=True)


# q0: Alice's unknown state
# q1: Alice's half of the Bell pair
# q2: Bob's half of the Bell pair

# Construct the quantum circuit
qc = qk.QuantumCircuit(3,3)


# Prepare Alice's unknown state q0 using the U-gate (Universal Single-Qubit Gate = Rz(phi)Ry(theta)Rz(lamda))
def prepare_state(qc, theta, phi):
    qc.u(theta, phi, 0 , 0)


# Create the Bell state q1<->q2
def create_bell_pair(qc):
    qc.h(1)
    qc.cx(1,2)


# Transmit the quantum state of q0 to q2
def teleportation(qc):
    # Step 1 Prepare Alice's unkown state -> into Bell basis
    qc.cx(0,1)
    qc.h(0)

    # Step 2 Measure Alice's unknown state and half of the Bell pair
    qc.measure(0,0)
    qc.measure(1,1)

    # Step 3 Bob needs to use Alice's measured bits
    with qc.if_test((qc.clbits[0], 1)):
        qc.z(2)

    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)


#Verifying if the teleportation was successul by: U^{dagger} |Psi> = U^{dagger} U  |0> = |0>
def verify_teleportation(qc, theta, phi):
    qc.rz(-phi, 2)
    qc.ry(-theta, 2)
    qc.measure(2, 2)


def simulate_teleportation(qc):
    # Run simulation to verify the qc -> classical bits are displayed as c2c1c0
    circuit_simul = aer.AerSimulator()
    job = circuit_simul.run(qc, shots=1024)
    result = job.result()
    counts = result.get_counts()

    print(counts)


# Arbitrary state q0
random = np.random.default_rng()
theta = np.arccos(random.uniform(-1, 1))
phi = random.uniform(0, 2 * np.pi)

# Carrying out each step
prepare_state(qc, theta , phi)
create_bell_pair(qc)
teleportation(qc)
verify_teleportation(qc, theta , phi)

# Printing and saving the circuit
fig = qc.draw(output="mpl")
fig.savefig(images_folder / "quantum_teleportation_circuit.png")
plt.show()

# Simulating the experiment
simulate_teleportation(qc)