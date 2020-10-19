import matplotlib.pyplot as plt
import numpy as np

a = input(r'Enter side of a square: ')
r = (int(a) * np.sqrt(2)) / 2

x = np.linspace(-r-1, r+1, 100)
y = np.linspace(-r-1, r+1, 100)

fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(1,1,1)
rect = plt.Rectangle((0,0-r), int(a), int(a), angle = 45.0)
ax.add_patch(rect)

plt.plot(0, 0, marker='o', color = 'yellow')
X, Y = np.meshgrid(x, y)
F = X**2 + Y**2 
plt.contour(X, Y, F, [r**2])

plt.grid(True)
#plt.show()
plt.savefig('output.png', dpi = 400)