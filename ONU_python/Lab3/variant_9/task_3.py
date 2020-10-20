import matplotlib.pyplot as plt
import numpy as np


plt.subplot()
x1 = np.linspace(-2, -1, 100)
x2 = np.linspace(-1, 1, 100)
x3 = np.linspace(1, 2, 100)
plt.plot(x1, np.exp(x1+1), 'r-')
plt.plot(x2, x2**2, 'b--')
plt.plot(x3, pow((2-x3), 3), 'g-.')
plt.legend([r'$y = e^{x+1}$', r'$y = x^2 $', r'$y = (2 - x)^{3}$'])
plt.show()