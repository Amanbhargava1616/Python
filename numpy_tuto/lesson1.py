# Defining a multidimesnional array and using it and it's method

# (layers, rows, col)

import numpy as np

array_a = np.array([1, 2, 3, 4])

print(array_a)
print(f"Dimension of array_a: {array_a.ndim}")

array_b = np.array([[1, 2, 3], [4, 5, 6]])

print(array_b)
print(f"Dimension of array_b: {array_b.ndim}")
print(f"Shape of array_b: {array_b.shape}")

print(f"Accessing element in array: {array_b[1,0]}")


# reshaping a array
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(f"Array is: {arr3}, shape is: {arr3.shape}")

arr4 = arr3.reshape(2, 6)
print(f"Array is: {arr4}, shape is: {arr4.shape}")


# When a value is passed as -1 numpy will automaticaly calculate numbers of columns or rows required
arr5 = arr3.reshape(-1, 1)
arr6 = arr3.reshape(1, -1)

print(arr5)
print(arr6)
