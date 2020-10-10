import numpy as np
from scipy.spatial import distance


def minimum(x):
    minn = x[0][1]
    i1 = 0
    j1 = 0
    for i in range(10):
        for j in range(10):
            if i != j and x[i][j] < minn:
                minn = x[i][j]
                i1 = i
                j1 = j
    return i1, j1


def two_dots():
    a = np.random.sample((10,2)) * 10
    x = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            x[i][j] = distance.chebyshev(a[i], a[j])
    ind_min = minimum(x)
    res = a[ind_min[0]]

    return f'Our dot is {res}'

print(two_dots())
