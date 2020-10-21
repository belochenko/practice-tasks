import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100, 1)
y1 = 4*x + 2
y2 = -7*x + 1
xpnt, ypnt = (0, 0)
plt.plot(x, y1, 'r-')
plt.plot(x, y2, 'y-')
plt.plot(xpnt, ypnt, linewidth = 2, markersize = 6, marker = 's', color = 'green')

plt.annotate(r'$y_{1}=4x+2$', xy = (-25,400), size = 10)
plt.annotate(r'$y_{2}=7x+1$', xy = (50,0), size = 10)
plt.annotate('A(0, 0)', xy = (5, 5), size = 12)

plt.show()
