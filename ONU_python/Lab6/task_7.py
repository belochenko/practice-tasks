import scipy.linalg as spla
import numpy as np

A = np.array([[12, -1, 3], [1, 10, 0], [-7, 2, 3]])

print(spla.norm(A, ord=2))  # 1

print(np.sqrt(np.max(spla.eigvals(A.T.dot(A)))))  # 2
