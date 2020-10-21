import matplotlib.pyplot as plt
import numpy as np

a = int(input("Size of a triangle side"))
rd = a / np.sqrt(3)
h = np.sqrt(3)/2*a
lst = [(-a/2, -(h-rd)), (0, rd), (a/2, -(h-rd))]
circle = plt.Circle((0, 0), rd, color='r', fill=False)
triangle = plt.Polygon(lst,color='b')
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.add_patch(triangle)
ax.add_patch(circle)
plt.axis('scaled')
plt.grid(True)
plt.savefig('output.png', dpi=400)
