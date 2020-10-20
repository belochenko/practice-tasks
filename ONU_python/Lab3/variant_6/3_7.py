import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = pow((np.sin(X ** 2) + np.cos(Y ** 2)), X * Y)

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