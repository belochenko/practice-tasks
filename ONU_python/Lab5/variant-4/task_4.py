import sympy as sp

x, a, n = sp.symbols('x a n')
f = (x ** n - a ** n) - (n * a ** (n - 1) * (x - a)) / (x - a) ** 2
res = sp.limit(f, x, a)
sp.pprint(res)