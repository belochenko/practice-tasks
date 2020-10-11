import numpy as np

array1 = np.random.randint(1, 10, size=(10, 2))
print(f'Input{array1}')

a = np.array([[-5, 1]])
array2 = np.tile(a, (10, 1))
res1 = array1 + array2
print(f'First task: {res1}')

distance = np.zeros(10)
distance = np.linalg.norm(res1, axis=1)
min_distance = np.argmin(distance)
res2 = res1[min_distance]
print(f'Second task: {res2}')

indexes = np.argsort(distance)
res3 = res1[indexes]
print(f'Third task: {res3}')

greater_0 = res3.clip(min = 0)
positive = np.prod(greater_0, axis = 1)
positive_idx = np.where(positive > 0)
res4 = res3[positive_idx]
print(f'Fourth task: {res4}')