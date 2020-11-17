import sympy as sp

x, y = sp.symbols('x y')
f = sp.exp(x ** 2 + y ** 2) / sp.sqrt(x * y)
res1 = f.diff(x)
res2 = f.diff(y)
res3 = f.diff(x, 2)
res4 = f.diff(y, 2)
print(f'df/dx = {sp.simplify(res1)}')
print(f'df/dy = {sp.simplify(res2)}')
print(f'd^2f/dx^2 = {sp.simplify(res3)}')
print(f'd^2f/dy^2 = {sp.simplify(res4)}')