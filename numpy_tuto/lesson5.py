# Aggregation Functions

import numpy as np

arr = np.array([[1, 2, 34, 4, 5, 6], [5, 3, 7, 1, 2, 3]])

print(np.sum(arr))
print(np.sum(arr, axis=1))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.mean(arr))
print(np.std(arr))
