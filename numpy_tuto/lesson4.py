# Broadcasting

# From right to left and only if both values are either same or one of them is 1

import numpy as np

arr1 = np.array([[[1], [2], [3]], [[4], [5], [6]]])

arr2 = np.array([[[1, 2, 3, 4]]])

print(arr1.shape)
print(arr2.shape)

print(arr1 + arr2)
print("------------------------------------")
print(arr1 - arr2)
print("------------------------------------")
print(arr1 * arr2)
print("------------------------------------")
print(arr1 / arr2)
