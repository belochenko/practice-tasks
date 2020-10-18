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

arr = np.array([[4, 9, -3, 0, 2], [-1, 3, 3, 8, -5], [-2, 3, 7, 4, 6], [1, 2, -4, 1, 9], [-1, 3, 5, -2, 8]])

print(f'Is this matrix meets Sylvesters criterion? {silv(arr)}')
