import sympy as sp

x = sp.symbols('x')
f = (x ** 2) * sp.exp(x)
res = sp.integrate(f, (x, 0, 1))
sp.pprint(res)
