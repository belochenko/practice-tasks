import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-np.pi,np.pi, 50)
x2 = np.linspace(-2, 2, 50)

fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.plot(x1, np.sin(x1**2), 'b-')
plt.plot(x1, np.cos(x1**2), 'r-.')
plt.plot(x2, x2/20, 'y:')
plt.plot(x2,np.exp(x2), 'g--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function')
ax.legend(["$f = sin(x^{2})$","$g = cos(x^{2})$", "$u = x / 20$","$v = e^{x}$"])
plt.grid(True)


fig = plt.figure(figsize = (10, 10))
x1 = np.linspace(-np.pi,np.pi, 50)
x2 = np.linspace(-2, 2, 50)
y1 = np.sin(x1**2)
y2 = np.cos(x1**2)
y3 = x2/20
y4 = np.exp(x2)

ax = fig.add_subplot(1, 2, 1)
plt.plot(x1, y1,'b-')
plt.plot(x1, y2, 'r-.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function №1')
ax.legend(["$f = sin(x^{2})$","$g = cos(x^{2})$"])
plt.grid(True)

ax = fig.add_subplot(1, 2, 2)
plt.plot(x2, y3, 'y:')
plt.plot(x2, y4, 'g--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function №2')
ax.legend(["$u = x / 20$","$v = e^{x}$"])
plt.grid(True)

plt.show()