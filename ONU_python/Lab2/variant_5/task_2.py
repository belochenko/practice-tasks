import numpy as np

arr1 = np.array([[-2,-2,1,1,1,1]])
a = np.array([[1, 1]])
arr2 = np.tile(a, (4, 1))
b = np.diagflat([[3,3],[3,3]])
c = np.concatenate((arr2, b), axis = 1)

block_matrix = np.concatenate((arr1, arr1, c), axis = 0)
print(block_matrix)

s = 0

for i in range(5):
    for j in range(5):
        s +=  block_matrix[i][i+1]
        break
print(s)