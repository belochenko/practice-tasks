import sympy as sp

x, y, z = sp.symbols('x y z')

equation = [
    sp.Eq(x * y - z ** 2, 1),
    sp.Eq(y * z - x ** 2, 2),
    sp.Eq(z * x - y ** 2, 3)
]
res = sp.solve(equation)
sp.pprint(res)
