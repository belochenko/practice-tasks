from scipy.misc import derivative
import numpy as np

f = lambda x: np.sin(x)
res1 = derivative(f, np.pi, dx=1e-5)
print(res1)
res2 = derivative(f, np.pi, n=2, dx=1e-5)
print(res2)
h = 1e-5
func1 = (f(np.pi + h) - f(np.pi - h)) / (2 * h)
print(func1)
func2 = (f(np.pi - h) - 2 * f(np.pi) + f(np.pi + h)) / (h ** 2)
print(func2)