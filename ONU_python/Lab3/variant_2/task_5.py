import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-15, 15)
plt.grid(True)
y1 = 5*x1 + 3
y2 = 3*x1 - 7
plt.plot(x1, (y1), 'g-')
plt.annotate(r'$y1 = 5x + 3$', xy = (10,50), size = 10)
plt.plot(x1, (y2), 'b-')
plt.annotate(r'$y2 = 3x - 7$', xy = (9,15), size = 10)
plt.plot(-5, -21.7, marker='o', color='red')
plt.annotate('A(-5, -21)', xy = (-5, -31), size = 15)

plt.show()
