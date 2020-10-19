import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-1, 1)
x2 = np.linspace(0, 1)
f = (x1**3) + 2*(x1**2) + 1
g = (x1-1)**4
u = x2**(1/2)
v = np.exp(-x2**2)

plt.subplot(221)
plt.plot(x1, f)
plt.title(r'$f = x**3 + 2x**2 + 1$')
plt.grid(True)

plt.subplot(222)
plt.plot(x1, g)
plt.title(r'$g = (x1-1)**4$')
plt.grid(True)

plt.subplot(223)
plt.plot(x2, u)
plt.title(r'$u = sqrt(x)$')
plt.grid(True)

plt.subplot(224)
plt.plot(x2, v)
plt.title(r'$v = e**(-x**2)$')
plt.grid(True)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x1, f, 'r-')
plt.plot(x1, g, 'y--')
plt.plot(x2, u, 'g_')
plt.plot(x2, v, 'b-.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графики')
ax.legend(["$f = {x**3 + 2x**2 + 1}$", "$g = (x1-1)**4$", "$u = sqrt(x)$", "$v = e**(-x**2)$"])
plt.grid(True)

plt.show()
