  
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

r = input(r'Enter radius of a circle: ')
a = int(r) / pow(3, 0.5)
r = int(r)

x = np.linspace(-r-1, r+1, 100)
y = np.linspace(-r-1, r+1, 100)

fig = plt.figure(figsize = (7, 7))
ax = fig.add_subplot(1,1,1)
triangle = mpatches.RegularPolygon([0, 0], 3, r)
ax.add_patch(triangle)

plt.plot(0, 0, marker='o', color = 'red')
X, Y = np.meshgrid(x, y)
F = X**2 + Y**2 
plt.contour(X, Y, F, [r**2])

plt.grid(True)
plt.savefig('output.png', dpi = 400)