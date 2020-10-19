import numpy as np
import random

a = np.random.uniform(-1,1,5)
b1 = (1 - a**2) ** 0.5
b2 = -(1 - a**2) ** 0.5



def point2angle(a, b):
    r = (np.arctan2(b,a))
    r = r / np.pi
    return r % 2

def min_angle(a, b, c):
    index_min = np.argmin(a)
    x = b[index_min]
    y = c[index_min]
    return x, y

array1 = point2angle(a, b1)
array2 = point2angle(a, b2)
array = np.concatenate((array1, array2))
print(array)
print(min_angle(array, a, b1))
sorted_array = np.sort(array)  #3 task
print(sorted_array)
np.clip(sorted_array, 0, 1)  #4 task
print(sorted_array)









