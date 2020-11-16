import sympy as sp

e, x = sp.symbols("e x")
res = sp.solve(sp.exp(4*x) - sp.exp(x) - 2, x)
sp.pprint(res)

