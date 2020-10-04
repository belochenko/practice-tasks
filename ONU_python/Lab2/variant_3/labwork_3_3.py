import numpy as np

def Silverster(a):
    n = len(a)
    check = True
    for i in range(n):
        a1 = a[0: i, 0: i]
        if np.linalg.det(a1) <= 0:
            check = False
            break
    return check

arr1 = np.array([[-2, 8, 8, 4, -3], [3, 0, -1, 3, 0], [7, -2, -4, 6, 2], [7, -5, 1, -5, -3], [-2, -5, 7, 6, -1]])
arr2 = np.array([[14, 6, 3], [6, 9, -4], [3, -4, 9]])

print(Silverster(arr1))
print(Silverster(arr2))