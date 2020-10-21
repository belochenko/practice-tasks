import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, np.pi*4, 50)
y1 = np.exp(-t)
y2 = np.sin(t)

plt.plot(t, y1, 'b-')
plt.plot(t, y2, 'b-')
plt.show()
