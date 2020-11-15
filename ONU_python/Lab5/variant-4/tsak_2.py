import sympy as sp

e, x = sp.symbols("e x")
res = sp.solve(e ** (4 * x) - e ** (2 * x) - 1, x)
sp.pprint(res)