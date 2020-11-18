import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')
f = y(x).diff(x, 3) - y(x) - x * sp.exp(x)
sp.pprint(sp.dsolve(f, y(x)))