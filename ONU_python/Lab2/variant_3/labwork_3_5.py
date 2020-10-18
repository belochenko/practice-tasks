import numpy as np

def function():
    matrix = np.genfromtxt('input.csv', dtype=int, delimiter=',')
    matrix[0][0] = np.sum(matrix)
    np.savetxt('output.csv', matrix, fmt='%.0f')

function()
