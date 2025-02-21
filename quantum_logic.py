from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def apply_superposition():
    """Simulates a quantum move and displays the circuit in the terminal"""
    qc = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit
    qc.h(0)  # Apply Hadamard gate for superposition
    qc.measure(0, 0)  # Measure the qubit

    # Display the quantum circuit in the terminal
    print("Quantum Circuit for Superposition:")
    print(qc.draw(output='text'))

    # Execute quantum circuit and get the result
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    measurement = result.get_counts()
    return 'X' if '0' in measurement else 'O'

def apply_entanglement():
    """Simulates entangled moves and displays the circuit in the terminal"""
    qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits
    qc.h(0)  # Apply Hadamard gate to create superposition
    qc.cx(0, 1)  # Entangle qubits 0 and 1
    qc.measure([0, 1], [0, 1])  # Measure both qubits

    # Display the quantum circuit in the terminal
    print("Quantum Circuit for Entanglement:")
    print(qc.draw(output='text'))

    # Execute quantum circuit and get the result
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    measurement = list(result.get_counts().keys())[0]
    return ('X', 'X') if measurement == '00' else ('O', 'O')
