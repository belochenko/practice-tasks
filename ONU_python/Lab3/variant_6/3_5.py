import matplotlib.pyplot as plt
import numpy as np

plt.subplot()
x = np.linspace(-10, 10, 20)
plt.grid(True)

plt.plot(x, (-3 * x + 5), 'r-')
plt.plot(x, (2 * x - 4), 'b-')
plt.plot(1.8, -0.4, marker = 'o')

plt.annotate(r'$y_{1}= -3x + 5$', xy = (-10,18), size = 10)
plt.annotate(r'$y_{2}= 2x - 4$', xy = (5, 15), size = 10)
plt.annotate('A(1.8, -0.4)', xy = (-0.5, -9), size = 12)

plt.show()