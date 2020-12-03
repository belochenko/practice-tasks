import numpy as np
import scipy.integrate as spint

f = lambda x: x**2*np.log(x)

print(f' #1 = {spint.quad(f, 0, 1)}')
print(f' #2 = {spint.fixed_quad(f, 0, 1, n=10)}')
print(f' #3 = {spint.quadrature(f, 0, 1, tol=1e-10)}')
