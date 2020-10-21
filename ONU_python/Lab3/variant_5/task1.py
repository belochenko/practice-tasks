import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-0.5, 0.5, 50)
x2 = np.linspace(-0.6, 0.5, 50)

plt.subplot(221)
plt.plot(x1, np.power(np.fabs(2*x1), 3))
plt.title(r'$f (x) = |2x|^3$')
plt.grid(True)

plt.subplot(222)
plt.plot(x1, np.power(np.fabs(2*x1), 5))
plt.title(r'$g (x) = |2x|^5$')
plt.grid(True)

plt.subplot(223)
plt.plot(x2, np.sqrt(np.fabs(x2)))
plt.title(r'$u (x) = \sqrt{|x|}$')
plt.grid(True)

plt.subplot(224)
plt.plot(x2, np.power(x2, 1/5))
plt.title(r'$v (x) = x^{1/5}$')
plt.grid(True)


fig, ax = plt.subplots()
x1 = np.linspace(-0.5, 0.5, 50)
x2 = np.linspace(-0.6, 0.5, 50)
y1 = np.power(np.fabs(2*x1), 3)
y2 = np.power(np.fabs(2*x1), 5)
y3 = np.sqrt(np.fabs(x2))
y4 = np.power(x2, 1/5)
plt.plot(x1, y1,'r--')
plt.plot(x1, y2, 'b-')
plt.plot(x2, y3, 'g-.')
plt.plot(x2, y4, 'y:')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graphics')
ax.legend(["$f (x) = |2x|^3$","$g (x) = |2x|^5$","$u (x) = \sqrt{|x|}$","$v (x) = x^{1/5}$"])
plt.grid(True)

plt.show()