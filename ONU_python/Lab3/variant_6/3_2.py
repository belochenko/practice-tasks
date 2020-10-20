import matplotlib.pyplot as plt
import numpy as np

plt.subplot(polar = True)
phi = np.arange(0, 2*np.pi, 0.01)
func = np.sin(6 * phi)
plt.plot(phi, func, 'm^', lw = 5)
plt.show()