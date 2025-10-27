from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.primitives import BackendSamplerV2 as BackendSampler

def quantum_rng(num_bits=8):
    qrng_circuit = QuantumCircuit(num_bits)
    for i in range(num_bits):
        qrng_circuit.h(i)
    qrng_circuit.measure_all()

    simulator = AerSimulator()
    sampler = BackendSampler(backend=simulator)

    result = sampler.run([qrng_circuit], shots=1).result()
    bitstring_dict = result[0].data
    bit_array = list(bitstring_dict.values())[0]

    # Corrected conversion from BitArray to binary string
    # The BitArray object is iterable.
    random_binary_string = ''.join([str(int(b)) for b in bit_array[0]])
    random_integer = int(random_binary_string, 2)

    return random_integer, random_binary_string

# Run
random_number, binary_bits = quantum_rng(num_bits=8)
print(f"Generated a {len(binary_bits)}-bit quantum random number.")
print(f"Binary string: {binary_bits}")
print(f"Decimal value: {random_number}")
