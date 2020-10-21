import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 1, 50)
x2 = np.linspace(1, np.pi/2, 50)
x3 = np.linspace(3, 5, 50)
y1 = np.sqrt(x1)
y2 = 1
y3 = (x3-4)**2
plt.plot(x1, y1, 'r--')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'g-')
plt.show()