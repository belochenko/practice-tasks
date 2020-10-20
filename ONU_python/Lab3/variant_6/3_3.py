import matplotlib.pyplot as plt
import numpy as np


plt.subplot()
x1 = np.linspace(-2, -1, 100)
x2 = np.linspace(-1, 1, 100)
x3 = np.linspace(1, 3, 100)
plt.plot(x1, abs(x1) - 2, 'r-')
plt.plot(x2, np.sin((np.pi/2)*x2), 'b--')
plt.plot(x3, pow((2-x3), 3), 'g-.')
plt.legend([r'$y = \left | x \right | - 2$', r'$y = \sin (\frac{\pi}{2}x)$', r'$y = (2 - x)^{3}$'])
plt.show()