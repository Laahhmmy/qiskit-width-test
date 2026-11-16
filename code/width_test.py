from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError

# A "shot" is one run of a circuit. Run each circuit 1,000 times.
shots = 1000

# Give every measured qubit a 5% chance of being recorded incorrectly.
# Each row represents the actual bit, and each column represents the recorded bit.
# Actual 0: record 0 with 95% probability or 1 with 5% probability.
# Actual 1: record 0 with 5% probability or 1 with 95% probability.
noise_model = NoiseModel()
noise_model.add_all_qubit_readout_error(
    ReadoutError([[0.95, 0.05], [0.05, 0.95]])
)
simulator = AerSimulator(noise_model=noise_model)

# Width is the number of qubits in the circuit.
for width in [2, 4, 6]:
    # Qubits start in state |0⟩. Measure all of them without applying any gates.
    circuit = QuantumCircuit(width)
    circuit.measure_all()

    # Run the circuit and count how often each bit string appears.
    # For example, {"00": 903, "01": 45, "10": 49, "11": 3}.
    result = simulator.run(circuit, shots=shots).result()
    counts = result.get_counts()

    # Build the expected result: "00", "0000", or "000000".
    expected = "0" * width

    # Look up how many runs returned all zeros. Use 0 if that result never appeared.
    correct_runs = counts.get(expected, 0)

    # Any run with at least one 1 counts as one incorrect run.
    incorrect_runs = shots - correct_runs
    error_rate = 100 * incorrect_runs / shots

    # Displays the percentages of incorrect runs for each circuit width.
    print(f"{width} qubits: {incorrect_runs}/{shots} incorrect ({error_rate:.1f}%)")