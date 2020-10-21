import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 1, 50)
x2 = np.linspace(1, np.pi/2, 50)
x3 = np.linspace(np.pi/2, np.pi, 50)
y1 = np.arcsin(x1) - 1
y2 = np.pi/2 - x2
y3 = np.cos(x3)
plt.plot(x1, y1, 'r--')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'g-')
plt.show()