import numpy as np

def check_rule(arr):
    return (arr == arr[0]).all()



def sum_of_matrix(mat):
    sum_of_columns = mat.sum(axis=0)
    sum_of_rows = mat.sum(axis=1)
    glav_diag = np.sum(np.diagonal(mat))
    pob_diag = np.sum(np.diagonal(np.fliplr(mat)))


    a = np.concatenate((sum_of_columns, sum_of_rows))
    b = np.append(a, (glav_diag, pob_diag))

    return check_rule(b)


a = [[1,2], [2,1]]
r = sum_of_matrix(np.array(a))
print(r)
