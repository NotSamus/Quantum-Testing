import pennylane as qml
from pennylane import numpy as np


num_layers = 2
num_qubits = 16
dev = qml.device("default.qubit", wires=num_qubits)
weights = np.random.uniform(low=0, high=2*np.pi, size=(num_layers, num_qubits))
print("This is the manually print of the weights, one time")
for w in weights:
    print([w])

print("This is for testing")
epochs = 20
def circuit(weights):
    for i in range(len(weights)):
        qml.RY(weights[i], wires=i)

@qml.qnode(dev)
def quantum_model(weights):
    circuit(weights)
    return qml.expval(qml.PauliZ(0))

def cost(weights):
    prediction = quantum_model(weights)
    return (prediction - label) ** 2

opt = qml.AdamOptimizer(0.1)
weights = np.random.rand(num_qubits)

for _ in range(100):
    weights = opt.step(cost, weights)

for epoch in range(epochs):
    weights = opt.step(cost_fn, weights)
    print(f"Epoch {epoch} , weights: {weights}")
