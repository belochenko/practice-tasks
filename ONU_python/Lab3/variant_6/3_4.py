import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 3 * np.pi, 100)

plt.plot(t, np.exp(t * (-1)) * np.cos(t))
plt.plot(t, np.exp(t) * np.sin(t))
plt.legend([r'$y = e^{-t} cos(t)$', r'$y = e^{t} sin (t)$'])
plt.show()