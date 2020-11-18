import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')
sp.pprint(sp.dsolve(y(x).diff(x, 2) - 3*y(x).diff(x) + y(x) - sp.cos(x), y(x)))

