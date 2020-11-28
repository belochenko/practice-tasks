import scipy.integrate as sp
import numpy as np

f = lambda y, x: x * np.sin(y)
res = sp.dblquad(f, 0, np.pi / 2, lambda x: x - (np.pi / 6), lambda x: x + (np.pi / 6))
print(f'The double integral is: {res[0]}')
