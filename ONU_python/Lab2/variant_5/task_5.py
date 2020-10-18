import numpy as np
import csv

with open('input.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = np.array(list(reader)).astype(float)
   
    matrix = np.array(data, dtype = np.int)
    negative = np.sum(matrix[matrix < 0])
    new_element = np.abs(negative)
    sum_of_neg = 0
    sum_of_neg += new_element

    new_matrix = np.where(matrix < 0, new_element, matrix)
    str_matrix = str(new_matrix)
    with open("output.csv", "w") as output:
        output.write(str_matrix)
            