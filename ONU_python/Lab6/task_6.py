import scipy.linalg as spl
import numpy as np

A = np.array([[-1, 6], [2, 7], [-1, 5]])
b = np.array([1, 1, 1])

print(spl.solve(A.T.dot(A), A.T.dot(b)))  # 1

x2, res, rank, s = spl.lstsq(A, b)
print(x2)  # 2

Q, R = spl.qr(A, mode='economic')
x3 = spl.inv(R).dot(Q.T.dot(b))
print(x3)  # 3

U, s, VT = spl.svd(A, full_matrices=False)
x4 = VT.T.dot(spl.inv(np.diag(s)).dot(U.T.dot(b)))
print(x4)  # 4
