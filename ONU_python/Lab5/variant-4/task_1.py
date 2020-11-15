import sympy as sp

a = sp.Symbol('a', real=True)
y = sp.simplify( sp.sqrt((a ** 3 - 6 * a ** 2 + 12 * a - 8) * (a ** 2 - 5) * (a + 1)) ** 4) / ((a ** 2 - 4 * a + 3) / (sp.sqrt(a + 1) ** 4) )
res = y.evalf(subs={a:6})
print(f'The answer for a = 6 is: {res}')
