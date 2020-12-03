from scipy.misc import derivative
import numpy as np


def first(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def second(x, h):
    return (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2)


f = lambda x: np.exp(x ** 2)

print(derivative(f, 0, dx=1e-06))  # 1
print(derivative(f, 0, dx=1e-06, n=2))  # 2

print(first(0, 1e-06))  # func1
print(second(0, 1e-06)) # func2
