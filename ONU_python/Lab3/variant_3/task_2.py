import matplotlib.pyplot as plt
import numpy as np

plt.subplot(polar=True)
phi = np.arange(0, 2*np.pi, 0.01)
func = 1 - np.sin(phi)
plt.plot(phi, func, color='orange', marker='^', ms=3, lw=3)
plt.show()
