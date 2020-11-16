import sympy as sp

a = sp.Symbol('a', real=True)
y = sp.simplify(sp.sqrt((a ** 3 - 3 * a ** 2 + 3 * a - 1) * (a ** 2 - 4) * (a - 2)) ** 4) / ((a ** 2 - 4 * a + 3) / (sp.sqrt(a + 2) ** 4))
res = y.evalf(subs={a: 4})
print(f'The answer for a = 4 is: {res}')

