import numpy as np

def silv(a):
    n = len(a)
    check = True
    for i in range(n):
        a1 = a[0: i, 0: i]
        if np.linalg.det(a1) <= 0:
            check = False
            break
    return check

arr = np.array([[22, -9, 7], [-9, 22, -19], [7, -19, 17]])

print(silv(arr))
