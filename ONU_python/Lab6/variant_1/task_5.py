import scipy.linalg as spla
import numpy as np

A = np.array([[1, -2, 3], [0, -4, 1], [-2, 5, 1]])
b = np.array([[1], [2], [3]])

res1 = spla.solve(A, b)
print('Gaussian Method:')
print(res1)
print()

inverted_A = spla.inv(A)
res2 = inverted_A.dot(b)
print('Matrix Method:')
print(res2)
print()

det = spla.det(A)
A1 = np.array([[1, -2, 3], [2, -4, 1], [3, 5, 1]])
det1 = spla.det(A1)
A2 = np.array([[1, 1, 3], [0, 2, 1], [-2, 3, 1]])
det2 = spla.det(A2)
A3 = np.array([[1, -2, 1], [0, -4, 2], [-2, 5, 3]])
det3 = spla.det(A3)
res3 = [[det1 / det], [det2 / det], [det3 / det]]
print('Cramer Method:')
print(res3)