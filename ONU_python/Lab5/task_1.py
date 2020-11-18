import sympy as sp

a = sp.Symbol('a', real=True)
y1 = (((a ** 3 - 3*(a ** 2) + 3*a - 1)*(a**2 - 4)*(a - 2))**(1/4))/((a**2 - 4*a - 5)/(a + 2)**(1/4))
sp.pprint(y1)
sp.pprint(sp.simplify(y1))
y2 = sp.factor(y1)
sp.pprint(y2)
sp.pprint(sp.simplify(y2))
print(y2.evalf(subs={a: 4}))


