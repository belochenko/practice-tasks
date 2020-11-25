import scipy.integrate as sp
import numpy as np

f = lambda x: np.log(x)
res1 = sp.quad(f, 0, 1)
print(res1[0])

res2 = sp.quadrature(f, 0, 1)
print(res2[0])

res3 = sp.fixed_quad(f, 0, 1)
print(res3[0])