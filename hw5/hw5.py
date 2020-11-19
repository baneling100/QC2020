from qiskit import (
    QuantumCircuit,
    execute,
    Aer)
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(4, 4)

circuit.h(0)
circuit.cx(0, 1)
circuit.cx(1, 2)
circuit.cx(2, 3)

circuit.measure(range(4), range(4))

simulator = Aer.get_backend('qasm_simulator')

job = execute(circuit, simulator, shots = 2000)
job.wait_for_final_state()

result = job.result()
counts = result.get_counts(circuit)

draw = circuit.draw(output = 'mpl')
draw.savefig('circuit.png')
hist = plot_histogram(counts)
hist.savefig('histogram.png')