import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
x = 9*np.sin(t/10)-1/2*np.sin((9*t)/10)
y = 9*np.cos(t/10)+1/2*np.cos((9*t)/10)

plt.plot(t, x)
plt.plot(t, y)
plt.legend([r'$x = 9 * sin(t/10) - 1/2 * sin(9t/10)$', r'$y = 9 * cos(t/10) + 1/2 * cos(9t/10)$'])
plt.show()
