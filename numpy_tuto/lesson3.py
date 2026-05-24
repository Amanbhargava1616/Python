import numpy as np

arr = np.array(
    [
        [1, 2, 3, 4],
        [5.555555, 6.1, 7.5, 8.87],
    ]
)

arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([5, 6, 7, 8])

# Scalar operations
print(arr + 1)
print(arr * 2)
print(arr / 2)
print(arr**3)
print(f"Dot Product is: {arr3.dot(arr2)}")


# Vectorised maths functions
print(np.sqrt(arr))
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))
