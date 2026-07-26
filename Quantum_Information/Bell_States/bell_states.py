import qiskit as qk
import qiskit_aer as aer
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from pathlib import Path

# Prepare for saving the results into the images folder
project_folder = Path(__file__).resolve().parent
images_folder = project_folder / "images"
images_folder.mkdir(exist_ok=True)

# Construct a function that creates Bell States
def create_bell_state(state):
    # Create a quantum circuit with 2 qubits
    qc = qk.QuantumCircuit(2)

    # Apply Hadamard gate to the first qubit
    qc.h(0)

    # Apply CNOT gate with control qubit 0 and target qubit 1
    qc.cx(0, 1)

    # Apply logic chain for specific state
    if state == "phi_plus":
        return qc
    
    elif state == "phi_minus":

        # Apply Z gate on qubit 0
        qc.z(0)
        return qc
    
    elif state == "psi_plus":

        # Apply NOT gate on qubit 0
        qc.x(0)
        return qc

    elif state == "psi_minus":

        # Apply both X and Z gates on qubit 0
        qc.x(0)
        qc.z(0)
        return qc
    
    else:
        raise ValueError("Unknown Bell state.")


# Construct a function that simulates the circuit
def simulate_bell_state(circuit, state):
    
    state_simul = aer.StatevectorSimulator()

    circuit_simul = aer.AerSimulator()

    # Inspect the unmeasured quantum state
    state_job = state_simul.run(circuit)
    state_result = state_job.result()
    statevector = state_result.get_statevector()

    print(statevector)

    # Add measurements for the shot experiment
    measured_circuit = circuit.copy()
    measured_circuit.measure_all()

    # Run simulation
    job = circuit_simul.run(measured_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts()

    print(counts)

    #Show the measured circuit
    fig = measured_circuit.draw(output="mpl")
    fig.savefig(images_folder / f"{state}_circuit.png")
    plt.show()

    #Plot results
    hist = plot_histogram(counts)
    hist.savefig(images_folder / f"{state}_histogram.png")
    plt.show()

    return statevector, counts


# Create list with all the Bell States
states = ["phi_plus", "phi_minus", "psi_plus", "psi_minus"]


# Carry out each experiment using a for loop
for state in states:

    # Simulation
    bell = create_bell_state(state)
    print(f"\nState: {state}")
    simulate_bell_state(bell, state)