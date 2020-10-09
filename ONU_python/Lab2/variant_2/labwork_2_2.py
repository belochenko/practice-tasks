import numpy as np
import math

a = np.array([[1, -1]])
b = np.array([[3, -2]])
array = np.tile(a, (6, 1))
array1 = np.tile(b, (6, 1))

A = np.concatenate([array, array1, array], axis = 1)

A = np.fabs(A)

s = np.sum(A)
        
print(int(s))