import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.01, 2*np.pi, 50)
x2 = np.linspace(0, 2*np.pi, 50)

plt.subplot(221)
plt.plot(x1, np.sin(x1)/x1)
plt.title(r'$f = sin(x)/x$')
plt.grid(True)

plt.subplot(222)
plt.plot(x1, np.exp(-x1) * np.cos(x1))
plt.title(r'$g = e^{-x}cos(x)$')
plt.grid(True)

plt.subplot(223)
plt.plot(x2, np.sin(np.log1p(x2)))
plt.title(r'$u = sin(ln(x+1))$')
plt.grid(True)

plt.subplot(224)
plt.plot(x2, np.cos(np.log1p(x2)))
plt.title(r'$v = cos(ln(x+1))$')
plt.grid(True)


fig, ax = plt.subplots()
x1 = np.linspace(0.01, 2*np.pi, 50)
x2 = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x1)/x1
y2 = np.exp(-x1) * np.cos(x1)
y3 = np.sin(np.log1p(x2))
y4 = np.cos(np.log1p(x2))
plt.plot(x1, y1,'r--')
plt.plot(x1, y2, 'b-')
plt.plot(x2, y3, 'g-.')
plt.plot(x2, y4, 'y:')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graphics')
ax.legend(["$f = {sin(x)/x}$","$g = e^{-x}cos(x)$","$u = sin(ln(x+1))$","$v = cos(ln(x+1))$"])
plt.grid(True)

plt.show()
