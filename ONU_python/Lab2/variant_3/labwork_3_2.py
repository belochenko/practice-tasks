import numpy as np

arr1 = np.arange(6, 0, -1) 
arr2 = np.arange(-6, 0, 1)
arr3 = 2*np.ones((2, 6))
arr4 = 4*np.ones((2, 6))
A1 = np.vstack((arr1, arr2, arr3, arr4))
A2 = A1**3
print(A2.min())