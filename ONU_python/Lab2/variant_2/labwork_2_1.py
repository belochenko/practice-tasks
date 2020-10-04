import numpy as np
import random

a = np.random.uniform(-1,1,10)
b = np.zeros(10)
for i in range(0, 10, 2):
    tmp = 1 - pow(a[i], 2)
    b[i] = pow(tmp, 0.5)
    b[i + 1] = b[i] * (-1)


def point2angle(a, b):
    r = (np.arctan2(b,a))
    r = r / np.pi
    return r % 2

def min_angle(a, b, c):
    index_min = np.argmin(a)
    x = b[index_min]
    y = c[index_min]
    return x, y


array = point2angle(a, b)
print(array)
print(min_angle(array, a, b))
sorted_array = np.sort(array)  #3 task
print(sorted_array)
sorted_array = [x for x in sorted_array if x < 0.5]  #4 task
print(sorted_array)








