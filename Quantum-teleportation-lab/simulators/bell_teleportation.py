# Developed by Jesus Lopez

import numpy as np
from numpy import kron
from typing import Tuple

# Define basic states and gates
zero = np.array([[1], [0]])
one = np.array([[0], [1]])

kron = np.kron

H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])

def create_bell_state() -> np.ndarray:
    return (1 / np.sqrt(2)) * (kron(zero, zero) + kron(one, one))

print("Bell state:\n", create_bell_state())

