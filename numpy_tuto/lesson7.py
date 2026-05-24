# random

import numpy as np

rng = np.random.default_rng() # rng => random number generator

print(rng.integers(low=1, high=7))  # for a single value
print(rng.integers(low=1, high=7, size=(2)))  # for a 1-d array
print(rng.integers(low=1, high=7, size=(2, 7)))  # for a 2-d array
