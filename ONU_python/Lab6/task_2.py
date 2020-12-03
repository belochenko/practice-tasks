import scipy.integrate as spint
import numpy as np

f = lambda y, x: x * np.exp(y)
print(spint.dblquad(f, 0, 1, lambda x: x - 1, lambda x: x + 1))
