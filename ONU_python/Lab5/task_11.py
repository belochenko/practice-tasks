import sympy as sp

x = sp.symbols('x')
f = (x ** 2) * sp.exp(x)

sp.pprint(sp.integrate(f, (x, 0, 1)))
