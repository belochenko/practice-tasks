import sympy as sp

x, n, m = sp.symbols('x n m')
f = (((1 + m * x) ** n) - ((1 + n * x) ** m)) / (x ** 2)
res = sp.limit(f, x, 0)
sp.pprint(res)
