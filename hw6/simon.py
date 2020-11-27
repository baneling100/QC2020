from qiskit import(
    QuantumCircuit,
    execute,
    Aer)
from qiskit.visualization import plot_histogram
from qiskit.extensions import UnitaryGate
import numpy as np

circuit = QuantumCircuit(6, 3)

for i in range(3, 6):
    circuit.h(i)
circuit.barrier()

# oracle
f = [0b001, 0b011, 0b011, 0b001, 0b101, 0b111, 0b111, 0b101]
Uf = np.zeros((64, 64))
for i in range(64):
	Uf[(i & 0b111000) | (f[(i >> 3)] ^ (i & 0b111)), i] = 1

circuit.unitary(UnitaryGate(Uf), range(6), 'Uf')
circuit.barrier()

for i in range(3, 6):
    circuit.h(i)
circuit.barrier()

circuit.measure(range(3, 6), range(3))

simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots = 1000)

result = job.result()
counts = result.get_counts(circuit)
print("Total counts: ", counts)

draw = circuit.draw(output = 'mpl')
draw.savefig('simon_circuit.png', bbox_inches = 'tight')
hist = plot_histogram(counts)
hist.savefig('simon_histogram.png', bbox_inches = 'tight')
