import matplotlib.pyplot as plt
import numpy as np

plt.subplot(polar = True)
phi = np.arange(-8*np.pi, 8*np.pi, 0.1)
func = np.exp(np.sin(phi)) - 2*np.cos(4*phi) + np.power(np.sin((2*phi - np.pi)/(24)),5)
plt.plot(phi, func, color = 'purple', marker = 'o', markersize = 2, lw = 2)
plt.show()