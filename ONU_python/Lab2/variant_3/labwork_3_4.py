import numpy as np
from scipy.spatial import distance


a = np.random.randint(0, 10, size=(10, 2))
x = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        x[i][j] = distance.chebyshev(a[i], a[j])
s = x[0, x[0, :] > 0]

print(a[x.argmin() + 1])

