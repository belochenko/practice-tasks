import sympy as sp

x, y = sp.symbols('x y')
f = x ** 2 + x * (y ** 2)
grad1 = sp.diff(f, x)
grad2 = sp.diff(f, y)
res1 = int(grad1.evalf(subs={x: 1, y: 1}))
res2 = int(grad2.evalf(subs={x: 1, y: 1}))
print(f'df/dx = {grad1}')
print(f'df/dy = {grad2}')
print(f'Gradient of function f = ({grad1})i + ({grad2})j')
print(f'Gradient of function f at point M(1; 1) = ({res1})i + ({res2})j')

a = sp.sqrt((2 ** 2) + (-1 ** 2))
cosA = 2 / a
cosB = (-1) / a
final_res = res1 * cosA + res2 * cosB
print(f'Gradient of function f at point M(1; 1) in the direction of the vector a(2; -1) = {final_res}')

if final_res > 0:
    print('Function f increases in a direction of vector a(2; -1)')
elif final_res < 0:
    print('Function f decreases in a direction of vector a(2; -1)')
