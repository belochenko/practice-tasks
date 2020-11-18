import sympy as sp

a, x, t = sp.symbols('a x t')
u = (-1) / (2 * a) * sp.exp(sp.sqrt((x - t) ** 2) ** -a)
res = sp.simplify(u.diff(x, 2) - a ** 2 * u)
print(res)
