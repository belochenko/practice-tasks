import sympy as sp

x = sp.Symbol('x')
f = x ** 3 / (x ** 2 - x + 10)
res1 = sp.integrate(f, x)
sp.pprint(res1)

res2 = sp.simplify(sp.diff(res1))
sp.pprint(res2)
