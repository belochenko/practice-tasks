import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t*(t-2*np.pi))
y = np.sin(t) * np.cos(t)
plt.plot(x, y)

plt.legend([r'$x(t) = sin[t \cdot (t-2\pi)]$ ,$y(t) = sin (t) \cdot cos(t)$'])

plt.grid(True)
plt.show()