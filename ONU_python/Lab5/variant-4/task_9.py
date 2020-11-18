import sympy as sp

a, x, t = sp.symbols('a x t')
u = (-1) / (2 * a) * sp.exp(-a * sp.sqrt((x - t) ** 2))
res = sp.simplify(u.diff(x, 2) - (a ** 2 * u))
print(res == 0)