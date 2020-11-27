from qiskit import(
    QuantumCircuit,
    execute,
    Aer)
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(9, 8)

circuit.x(0)
circuit.barrier()

for i in range(9):
    circuit.h(i)
circuit.barrier()

# oracle
circuit.x(8)
for i in range(8, 0, -1):
    circuit.cx(i, i - 1)
for i in range(1, 8):
    circuit.cx(i + 1, i)
circuit.x(8)
circuit.barrier()

for i in range(9):
    circuit.h(i)
circuit.barrier()

circuit.measure(range(1, 9), range(8))

simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots = 1000)

result = job.result()
counts = result.get_counts(circuit)
print("Total counts: ", counts)

draw = circuit.draw(output = 'mpl')
draw.savefig('deutsch_circuit.png', bbox_inches = 'tight')
hist = plot_histogram(counts)
hist.savefig('deutsch_histogram.png', bbox_inches = 'tight')
