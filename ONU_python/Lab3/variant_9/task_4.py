import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)

plt.plot(t, np.sin(t*(t-2*np.pi)))
plt.plot(t, np.sin(t) * np.cos(t))
plt.legend([r'$x = sin[t \cdot (t-2\pi)]$', r'$y = sin (t) \cdot cos(t)$'])
plt.show()