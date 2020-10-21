import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)

x= 2 * np.sin(t)- (2 / 3 )*np.sin(2*t)
y= 2 * np.cos(t)- (2 / 3 )*np.cos(2*t)
plt.plot(x, y)
plt.legend([r'$x = 2sin(t) - \frac{2}{3}sin(2t), y = x = 2cos(t) - \frac{2}{3}cos(2t)$'])
plt.show()