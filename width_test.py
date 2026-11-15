from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError

shots = 1000

noise_model = NoiseModel()
noise_model.add_all_qubit_readout_error(
    ReadoutError([[0.95, 0.05], [0.05, 0.95]])
)
simulator = AerSimulator(noise_model=noise_model)

for width in [2, 4, 6]:
    circuit = QuantumCircuit(width)
    circuit.measure_all()

    result = simulator.run(circuit, shots=shots).result()
    counts = result.get_counts()

    expected = "0" * width
    correct_runs = counts.get(expected, 0)
    incorrect_runs = shots - correct_runs
    error_rate = 100 * incorrect_runs / shots

    print(f"{width} qubits: {incorrect_runs}/{shots} incorrect ({error_rate:.1f}%)")