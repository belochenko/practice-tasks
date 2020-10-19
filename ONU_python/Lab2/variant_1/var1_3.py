import numpy as np

def Silv(a):
    n = len(a)
    check = True
    for i in range(n):
        a1 = a[0: i, 0: i]
        if np.linalg.det(a1) <= 0:
            check = False
            break
    return check


a = np.array([[13, -13, -7],
[-13, 14, 9],
[-7, 9, 14]])

b = np.array([[3, 6, 2, -5, 5],
[4, 6, -5, 9, 1],
[-3, 3, 6, 8, -3],
[-1, 4, -1, 0, -5],
[4, -5, -4, -9, -5]])

print(Silv(a))
print(Silv(b))




