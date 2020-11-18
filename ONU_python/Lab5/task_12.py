import sympy as sp
import sympy.plotting as plt

u, v = sp.symbols('u v')

x1 = 4 + sp.sin(u)*(3 + sp.cos(v))
y1 = 4 + sp.cos(u)*(3 + sp.cos(v))
z1 = 4 + sp.sin(v)

x2 = sp.sin(u)*(1 + 0.2*v)
y2 = 0.2 * sp.sin(u) * sp.cos(v)
z2 = sp.cos(u)*(1 + 0.2*v)

plt.plot3d_parametric_surface((x1, y1, z1, (u, 0, 2*sp.pi), (v, 0, 2*sp.pi)), (x2, y2, z2, (u, -5, 5), (v, -5, 5)))
