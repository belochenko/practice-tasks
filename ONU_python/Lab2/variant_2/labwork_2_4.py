import numpy as np
from scipy.spatial import distance
import random
import math

def two_dots():
    a = np.random.sample((10,2)) * 20
    x = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            x[i][j] = distance.cityblock(a[i], a[j])


    ind_max = np.argmax(x)
    i1 = a[ind_max // 10]
    j1 = a[ind_max % 10]
    return f'Two dots {i1} and {j1}'
