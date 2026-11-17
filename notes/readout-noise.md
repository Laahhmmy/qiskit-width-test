

### 1. The QEM Zoo — Readout Error Mitigation

Readout errors happen when a qubit’s measurement is recorded incorrectly, such as when a `0` is reported as a `1`. An *ssignment matrix describes the probability of recording each output given the ideal result. Researchers can use this matrix to correct the measured distribution, but the correction can amplify statistical fluctuations and require more runs for a reliable estimate. [The QEM Zoo](https://qemzoo.com/)

### 2. Bravyi et al. (2021) — Mitigating Measurement Errors in Multiqubit Experiments

Bravyi and colleagues compared two models for measurement errors. One treats errors on each qubit as independent, while the other allows errors across qubits to be correlated. They tested their correction methods on IBM quantum hardware. The independent model is the closest match to our Qiskit simulation, where each qubit has a fixed 5% chance of being misread. [Bravyi et al.](https://doi.org/10.1103/PhysRevA.103.042605)

### Connection to our hypothesis

We count a run as incorrect if **at least one bit** is recorded incorrectly. With independent 5% readout errors, all \(n\) bits are correct with probability \(0.95^n\). The chance of at least one error is therefore \(1-0.95^n\). This predicts that a 6-qubit circuit will return an incorrect result more often than a 2-qubit circuit, even though each individual bit has the same error rate.

### References
Bravyi, S., Sheldon, S., Kandala, A., McKay, D. C., & Gambetta, J. M. (2021). Mitigating measurement errors in multiqubit experiments. Physical Review A, 103(4), Article 042605. https://doi.org/10.1103/PhysRevA.103.042605 doi.org

Russo, V. (n.d.). The QEM Zoo. Retrieved November 16, 2026, from https://qemzoo.com/