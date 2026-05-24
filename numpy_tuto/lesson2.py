import numpy as np

# Slicessing a multidimensional array

arr = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
)


print(arr[2:4, 1:3])

print(arr[2:, 2:3])
