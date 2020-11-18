import sympy as sp

x1, x2, y1, y2, a, b, t = sp.symbols("x1, x2, y1, y2, a, b, t")
u = 1 / ((2*a * sp.sqrt(t * sp.pi)) ** 2) * sp.exp(-((x1 - y1)**2 + (x2 - y2)**2)/(4 * (a**2) * t))
print(sp.simplify(u.diff(t)-a**2*(u.diff(x1, 2) + u.diff(x2, 2))))
