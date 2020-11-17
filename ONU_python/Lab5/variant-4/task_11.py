import sympy as sp

x = sp.Symbol('x')
f = x ** 4 * sp.exp(2 * x)
res = sp.integrate(f, (x, 0, 1))
sp.pprint(res)