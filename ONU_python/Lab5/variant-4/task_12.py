import sympy as sp
import sympy.plotting as plt

u, v = sp.symbols('u v')

x1 = 8 + (3 + sp.cos(v)) * sp.cos(u)
y1 = 3 + sp.sin(v)
z1 = 4 + (3 + sp.cos(v)) * sp.sin(u)

x2 = 0.4 + (0.3 + sp.cos(v)) * sp.cos(u)
y2 = 0.4 + sp.sin(v)
z2 = 0.4 + (0.3 + sp.cos(v)) * sp.sin(u)

plt.plot3d_parametric_surface((x1, y1, z1, (u, 0, 2*sp.pi), (v, 0, 2*sp.pi)), (x2, y2, z2, (u, 0, 2*sp.pi), (v, 0, 2*sp.pi)))