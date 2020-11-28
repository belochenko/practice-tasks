import scipy.integrate as sp
import numpy as np

f = lambda x: np.log(x)
res1 = sp.quad(f, 0, 1)
print(f'Integral #1 is: {res1[0]}')

res2 = sp.quadrature(f, 0, 1)
print(f'Integral #2 is: {res2[0]}')

res3 = sp.fixed_quad(f, 0, 1)
print(f'Integral #3 is: {res3[0]}')