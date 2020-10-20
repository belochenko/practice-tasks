import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.01, 2*np.pi, 50)
x2 = np.linspace(0, 2*np.pi, 50)

fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.plot(x1, np.sin(x1)/x1, 'b-')
plt.plot(x1, np.exp(-x1) * np.cos(x1), 'r-.')
plt.plot(x2, np.sin(np.log1p(x2)), 'y:')
plt.plot(x2, np.cos(np.log1p(x2)), 'g--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function')
ax.legend(["$f = sin(x)/x$","$g = e^{-x}cos(x)$", "$u = sin(ln(x+1))$","$v = cos(ln(x+1))$"])
plt.grid(True)


fig = plt.figure(figsize = (10, 10))
x1 = np.linspace(0.01, 2*np.pi, 50)
x2 = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x1)/x1
y2 = np.exp(-x1) * np.cos(x1)
y3 = np.sin(np.log1p(x2))
y4 = np.cos(np.log1p(x2))

ax = fig.add_subplot(1, 2, 1)
plt.plot(x1, y1,'b-')
plt.plot(x1, y2, 'r-.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function')
ax.legend(["$f = sin(x)/x$","$g = e^{-x}cos(x)$"])
plt.grid(True)

ax = fig.add_subplot(1, 2, 2)
plt.plot(x2, y3, 'y:')
plt.plot(x2, y4, 'g--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function')
ax.legend(["$u = sin(ln(x+1))$","$v = cos(ln(x+1))$"])
plt.grid(True)

plt.show()
