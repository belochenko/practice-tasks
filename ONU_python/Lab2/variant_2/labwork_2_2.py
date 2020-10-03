import numpy as np
import math

a = np.array([[1, -1]])
b = np.array([[3, -2]])
array = np.tile(a, (6, 1))
array1 = np.tile(b, (6, 1))

A = np.concatenate([array, array1, array], axis = 1)

s = 0
for i in range(6):
    for j in range(6):
        s += math.fabs(A[i][j])
print(s)