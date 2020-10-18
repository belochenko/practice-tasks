import numpy as np
import random
import math


def metric(a, b):
 x = pow((a[0] - b[0]),4) + pow((a[1] - b[1]),4)
 result = pow(x, 0.25)
 return result

def minimum(x):
    min = x[0][1]
    i1 = 0
    j1 = 0
    for i in range(10):
        for j in range(10):
            if i != j:
                if x[i][j] < min:
                    min = x[i][j]
                    i1 = i
                    j1 = j
    return i1, j1

def two_dots():
    a = np.random.sample((10,2)) * 20 -10
    x = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            x[i][j] = metric(a[i], a[j])

    indexes = minimum(x)
    i1 = a[indexes[0]]
    j1 = a[indexes[1]]
        
    return f'Two dots {i1} and {j1}'

print(two_dots())