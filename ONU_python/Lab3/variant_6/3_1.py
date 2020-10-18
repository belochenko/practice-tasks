import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)

plt.subplot(221)
plt.plot(x, x ** 2)
plt.title(r'$y = x ^ 2$')
plt.grid(True)

plt.subplot(222)
plt.plot(x, x ** 3)
plt.title(r'$y = x ^ 3$')
plt.grid(True)

plt.subplot(223)
plt.plot(x, x ** 4)
plt.title(r'$y = x ^ 4$')
plt.grid(True)

plt.subplot(224)
plt.plot(x, x ** 5)
plt.title(r'$y = x ^ 5$')
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