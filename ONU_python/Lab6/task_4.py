import scipy.integrate as spint
import matplotlib.pyplot as plt
import numpy as np


def f(y, t):
    y0, y1, y2 = y
    return [y1, y2, -3 - y1 - 2 * y2]


t = np.linspace(0, 10, 51)
y0 = [-1, 2, 3]
w = spint.odeint(f, y0, t)
print(w)

y1 = w[:, 0]
y2 = w[:, 1]
y3 = w[:, 2]
fig = plt.figure()
plt.plot(t, y1, '-g', t, y2, '-r', y3, '-b', lw=1)
plt.xlim(0, 10)
plt.show()
