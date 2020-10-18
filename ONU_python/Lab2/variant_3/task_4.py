import numpy as np
from scipy.spatial import distance
import random
import math



def two_dots():
    a = np.random.sample((10,2)) * 20 -10
    r = distance.cdist(a, a, 'chebyshev')

    # x = np.zeros((10, 10))
    # for i in range(10):
    #     for j in range(10):
            


    # ind_max = np.argmax(x)
    # i1 = a[ind_max // 10]
    # j1 = a[ind_max % 10]
    
    # return f'Two dots {i1} and {j1}'
    min_idx = np.where(r != 0)
    return min_idx[r[min_idx].argmin()]


print(two_dots())

