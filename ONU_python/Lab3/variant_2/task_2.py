import matplotlib.pyplot as plt
import numpy as np

plt.subplot(polar=True)
phi = np.arange(0, 8*np.pi, 0.01)
func = 2 * phi 
plt.plot(phi, func, color='green', marker='*', ms=1, lw=1)
plt.show()
