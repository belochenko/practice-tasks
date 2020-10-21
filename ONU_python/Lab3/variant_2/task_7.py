import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(1, 10, 100)
x1, y1 = np.meshgrid(x, y)
z = np.power(np.sin(x1), 2) * np.log(y1)

fig = plt.figure(figsize=(20, 15))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(x1, y1, z)

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(x1, y1, z)
ax.view_init(30, 45)

fig = plt.figure(figsize=(20, 15))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
p = ax.plot_surface(x1, y1, z)

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
p = ax.plot_surface(x1, y1, z)
ax.view_init(30, 45)

plt.show()
