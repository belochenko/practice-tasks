import numpy as np


def silverster(a):
    n = len(a)
    check = True
    for i in range(n):
        a1 = a[0: i, 0: i]
        if np.linalg.det(a1) <= 0:
            check = False
            break
    return check
