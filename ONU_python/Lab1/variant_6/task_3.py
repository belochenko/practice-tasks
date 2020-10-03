import numpy as np

def matrix(graf):
    a = np.asarray(graf).sum(axis = 0)
    return np.argmax(a) + 1



a = ([[0,1,0,1],
[1,0,1,1],
[0,1,0,0],
[1,1,0,0]])
print(matrix(a))