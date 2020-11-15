import sympy as sp

x, y, z = sp.symbols('x y z')

equation = [
    sp.Eq(x+ y+ z, 1),
    sp.Eq(x * y + y * z + z * x, 1),
    sp.Eq(x * y * z, 1)
]
res = sp.solve(equation)
sp.pprint(res)