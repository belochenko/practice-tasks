import sympy as sp

x, y = sp.symbols('x y')
f = x ** 3 - x * y
grad1 = f.diff(x)
grad2 = f.diff(y)
res1 = int(grad1.evalf(subs={x:1, y:1}))
res2 = int(grad2.evalf(subs={x:1, y:1}))
final_res = sp.sqrt(res1 ** 2 + res2 ** 2)
print(f'df/dx = {grad1}')
print(f'df/dy = {grad2}')
print(f'Gradient of function f = ({grad1})i + ({grad2})j')
print(f'Gradient of function f at point M(1; 1) = ({res1})i + ({res2})j')
print(f'|grad(f)| = {final_res}')

a = sp.sqrt((-1) ** 2 + (4) ** 2)
cosA = (-1) / a
cosB = (4) / a
res_f = res1 * cosA + res2 * cosB
print(f'Gradient of function f at point M(1; 1) in the direction of the vector a(-1; 4) = {res_f}')

if res_f > 0:
    print('Function f increases in a direction of vector a(-1; 4)')
elif res_f < 0:
    print('Function f decreases in a direction of vector a(-1; 4)')
