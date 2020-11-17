from sympy import *

x = symbols('x')
y = symbols('y',cls=Function)
diffeq = Eq(y(x).diff(x, x) - 3*y(x).diff(x) + y(x), cos(x))
pprint(dsolve(diffeq,y(x)))