import matplotlib.pyplot as plt
import numpy as np

phi = np.arange(0, 2*np.pi, 0.01)
func = np.power(np.sin(2 * phi), 3)

plt.polar(phi, func)
plt.plot(phi, func, color ='yellow', marker = 's', ms = 3, lw = 3)
plt.show()