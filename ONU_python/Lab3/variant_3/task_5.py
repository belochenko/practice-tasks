import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100, 1)
y1 = 6*x - 2
y2 = -x + 12
xcross, ycross = (2, 10)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(xcross, ycross, linewidth=2, markersize=6, marker='o', color='red')
plt.legend([r'$y1 = 6*x - 2$', r'$y2 = -x + 12$', r'$(x_{пересечения},y_{пересечения}) = (2,10)$'])
plt.show()
