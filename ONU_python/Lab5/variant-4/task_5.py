import sympy as sp

x = sp.Symbol('x')
f = sp.atan(1 / (1 - x))
res = sp.limit(f, x, 1, dir='-')
sp.pprint(res)