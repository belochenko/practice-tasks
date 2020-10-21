import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
(x1, y1) = np.meshgrid(x, y)
f = ((x1**2 + y1**2))**2 - (7 * (x1**2 - y1**2))
plt.contour(x1, y1, f, 0)
plt.show()