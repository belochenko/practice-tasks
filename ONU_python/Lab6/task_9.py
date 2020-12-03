import scipy.interpolate as spitp
import matplotlib.pyplot as plt
import numpy as np

n = np.array([0, 1, 2, 3, 4, 5])
x = np.array([-8, 3, 5, -1, 2, 0])
p = spitp.lagrange(n, x)
y = np.linspace(0, 5, 100)
L = p(y)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(n, x, 'm', label='Knots')
ax.plot(y, L, '--ro', label='Lagrange polynomial')

linear_interpolation = spitp.interp1d(n, x)
y_interp1 = linear_interpolation(y)
cubic_interpolation = spitp.interp1d(n, x, kind='cubic')
y_interp2 = cubic_interpolation(y)
ax.plot(n, x, 'yo', label='Knots')
ax.plot(y, y_interp1, 'g', label='Linear interpolation')
ax.plot(y, y_interp2, '--b', label='Cubic interpolation')
ax.legend(loc=0)

fig.show()
