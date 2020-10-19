import matplotlib.pyplot as plt
import numpy as np

plt.subplot()
x1 = np.linspace(-10, 10, 20)
plt.grid(True)

plt.plot(x1, (2*x1 - 5), 'r-')
plt.plot(x1, 3*x1, 'b-')
plt.plot(-5, -15, marker='o')

plt.annotate(r'$y_{1}=2x-5$', xy = (7,6), size = 10)
plt.annotate(r'$y_{2}=3x$', xy = (8,20), size = 10)
plt.annotate('A(-5, -15)', xy = (-5, -20), size = 15)

plt.show()
