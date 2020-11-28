from scipy.misc import derivative
import numpy as np

f = lambda x: np.sin(x)
res1 = derivative(f, np.pi, dx=1e-5)
print(f'Built in integral function of the first order is: {res1}')
res2 = derivative(f, np.pi, n=2, dx=1e-5)
print(f'Built in integral function of the second order is: {res2}')
h = 1e-5
func1 = (f(np.pi + h) - f(np.pi - h)) / (2 * h)
print(f'Difference formula integral of the first order is: {func1}')
func2 = (f(np.pi - h) - 2 * f(np.pi) + f(np.pi + h)) / (h ** 2)
print(f'Difference formula integral of the second order is: {func2}')