import sympy as sp

x = sp.symbols('x')
f = ((x ** 2) - 1) / ((x ** 3) + 5 * x)

res1 = sp.integrate(f, x)
sp.pprint(res1)

res2 = sp.simplify(sp.diff(res1))
sp.pprint(res2)


