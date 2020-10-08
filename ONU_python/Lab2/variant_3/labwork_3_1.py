import numpy as np

def  v2normalize(x):
    vector = np.linalg.norm(x)
    if vector == 0:
        return x
    else:
        return x/vector


array1 = np.random.randint(-10, 10, size=(10, 2))
distance = np.zeros(10)
distance = np.linalg.norm(array1, axis=1)
array2 = distance.argsort()
norm_array = np.zeros((10, 2))
norm_array = v2normalize(array1)
print(f"{array1[distance.argmax()]} - наиболее удаленная от начала координат точка")
print(f"{array1[array2]} - отсортированные в порядке возрастания длин векторов точки")
print(f"{norm_array} - массив нормированных векторов")
print(f"{norm_array[norm_array > 0]} - массив вектор с положительными координатами")
