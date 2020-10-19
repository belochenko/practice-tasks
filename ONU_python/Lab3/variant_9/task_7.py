import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-np.abs(X)) * (X**5 + Y**4) * np.sin(X*Y)

fig = plt.figure(figsize = (19, 15))

ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(X, Y, Z)

ax = fig.add_subplot(1, 2, 2, projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(X, Y, Z)
ax.view_init(30, 45)

#------------------------------------------------

fig = plt.figure(figsize = (19, 15))
ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
p = ax.plot_surface(X, Y, Z)

ax = fig.add_subplot(1, 2, 2, projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
p = ax.plot_surface(X, Y, Z)
ax.view_init(30, 45)

plt.show()