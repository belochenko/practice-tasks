import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X - 2*Y)**2 * np.exp(-abs(Y))

fig = plt.figure(figsize=(20, 15))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(X, Y, Z)

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(X, Y, Z)
ax.view_init(30, 45)

fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
p = ax.plot_surface(X, Y, Z)

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
p = ax.plot_surface(X, Y, Z)
ax.view_init(30, 45)

plt.show()