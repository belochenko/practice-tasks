import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
F = (X**2 + Y**2) - (7 * (X**2 - Y**2)) 
plt.contour(X, Y, F, [0])

plt.show()