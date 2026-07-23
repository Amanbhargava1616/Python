# filtering

import numpy as np

arr = np.array([[22, 4, 1, 3, 6, 4], [6, 88, 7, 3, 2, 1]])

gt_6 = arr[arr > 6]

btw_6_and_12 = arr[(arr > 6) & (arr < 12)]


print(gt_6)
print(btw_6_and_12)


arr_lt_5 = np.where((arr < 5) & (arr > 3), arr, 0)
print(arr_lt_5)
