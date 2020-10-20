import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)

first = plt.subplot(221)
plt.plot(x, x ** 2, 'r-')
plt.plot(x, x ** 3, 'b--')
plt.title(r'$f, g$')
first.set_xlabel('x')
first.set_ylabel('y')
first.legend(["y = x ** 2", "y = x ** 3"])
plt.grid(True)

second = plt.subplot(222)
plt.plot(x, x ** 4, 'r-')
plt.plot(x, x ** 5, 'b--')
plt.title(r'$u, v$')
second.set_xlabel('x')
second.set_ylabel('y')
second.legend(["y = x ** 4", "y = x ** 5"])
plt.grid(True)



fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y1 = x ** 2
y2 = x ** 3
y3 = x ** 4
y4 = x ** 5
plt.plot(x, y1,'r--')
plt.plot(x, y2, 'b-')
plt.plot(x, y3, 'g-.')
plt.plot(x, y4, 'y:')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graphics')
ax.legend(["y = x ** 2","y = x ** 3","y = x ** 4","y = x ** 5"])
plt.grid(True)

plt.show()