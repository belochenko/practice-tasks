import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
F = (X ** 2 + Y ** 2 - 3) * pow((X ** 2 + Y ** 2), 0.5) + np.sin(8*pow((X ** 2 + Y ** 2), 0.5)) * np.cos(6 * np.arctan(Y / abs(X))) - 0.75 * (np.sin(5 * np.arctan(Y / abs(X))) - 1)
plt.contour(X, Y, F, [0])

plt.show()