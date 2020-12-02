import scipy.linalg as spl
import numpy as np

A = np.array([[-6, 5, 2], [1, -3, 0], [4, -1, 9]])
b = np.array([1, 3, 2])

print(spl.solve(A, b))  # 1

AA = spl.inv(A)
print(np.dot(AA, b))  # 2

P, L, U = spl.lu(A)
Pb = P.T.dot(b)
y2 = spl.solve_triangular(L, Pb, lower=True)
x2 = spl.solve_triangular(U, y2, lower=False)
print(x2)  # 3
