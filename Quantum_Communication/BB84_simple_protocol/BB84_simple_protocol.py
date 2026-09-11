#Import necessary packages
import qiskit as qk
import numpy as np
import qiskit_aer as aer
from pathlib import Path


#Create path for image
script_directory = Path(__file__).resolve().parent
image_directory = script_directory / "images"
image_directory.mkdir(exist_ok=True)
image_path = image_directory / "bb84_simple_protocol.png"


#Create Alice's list of qbits that she wishes to send to Bob 
#(here it's a randomised list of x bits for the sake of the exercise)
number_of_qubits = int(input("Input a number of qubits Alice will send to Bob: "))
alice_b = np.random.randint(0, 2, size=number_of_qubits)


#Create Alice's bases Z = 0 and X = 1
alice_bases = np.random.randint(0, 2, size=number_of_qubits)


#Print both lists
print("Alice's bit list: ", alice_b ,  "Alice's bases list" , alice_bases)


#Create Quantum Circuit
qc = qk.QuantumCircuit(number_of_qubits, number_of_qubits)


#'Convert' classical bits to quantum bits
for i in range(number_of_qubits):
    #Z-basis check
    if alice_b[i] == 0 and alice_bases[i] == 0:
        qc.id(i)

    if alice_b[i] == 1 and alice_bases[i] == 0:
        qc.x(i)

    #X-basis check
    if alice_b[i] == 0 and alice_bases[i] == 1:
        qc.h(i)

    if alice_b[i] == 1 and alice_bases[i] == 1:
        qc.h(i)
        qc.z(i)


#Check if everything worked out as it should've
print(qc.draw(output="text"))
qc.barrier() #For cleaner circuit picture later


#Create Bob's bases (keeping the convention Z = 0 and X = 1)
bob_bases = np.random.randint(0, 2, size=number_of_qubits)
print("Bob's measurement bases are: ", bob_bases)


#Create for loop for Bob's procedure (comparing qbits, and measurement)
for i in range(number_of_qubits):
    if bob_bases[i] == 0:
        qc.measure(i,i)

    else:
        qc.h(i)
        qc.measure(i,i)



#Create a circuit simulation
circuit_simul = aer.AerSimulator()
compiled_qc = qk.transpile(qc, circuit_simul)
job = circuit_simul.run(compiled_qc, shots=1)
result = job.result()
counts = result.get_counts(compiled_qc)
print("Bob's measurement result:", counts)


#Create Bob's bit list
bob_result = list(counts.keys())[0]
bob_result = bob_result[::-1]
bob_b = [int(bit) for bit in bob_result]
print("Bob's measured bits:", bob_b)


#Plot the circuit
circuit_figure = qc.draw(output="mpl")
circuit_figure.savefig(image_path, bbox_inches="tight")
print("Circuit image saved to:", image_path)


#Create a list to check matching indices of the two lists
matching_indices = []


#Create for loop to check each indices between the two lists of A and B
for i in range(number_of_qubits):
    if alice_bases[i] == bob_bases[i]:
        matching_indices.append(i)

print("The matching bases indices (positions) are in the list: ",matching_indices) #-> Example: if result is [1, 3, 4], this means that the second, fourth and fifth bases indices matched


#Create the two sifted keys
alice_sk = []
bob_sk = []


#Append bits to the sifted keys
for i in matching_indices:
    alice_sk.append(int(alice_b[i]))
    bob_sk.append(bob_b[i])

print("Alice's sifted key:", alice_sk)
print("Bob's sifted key:  ", bob_sk)


#Verification message
if alice_sk == bob_sk:
    print("Success: Alice and Bob's sifted keys match.")
else:
    print("Error: Alice and Bob's sifted keys don't match.")