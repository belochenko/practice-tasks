import numpy as np

def function():
    matrix = np.genfromtxt('input.csv', dtype=int, delimiter=',')
    matrix2 = matrix.copy()
    matrix2[:, -1] = matrix[-1]
    matrix2[-1] = matrix[:,-1]
    np.savetxt('output.csv', matrix2, fmt='%.0f')

function()
