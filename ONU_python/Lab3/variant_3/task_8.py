import matplotlib.pyplot as plt

a = int(input("Enter the side of the square: "))
dr = a / 2
circle1 = plt.Circle((0, 0), dr, color='r', fill=True)
rect = plt.Rectangle((0+dr, 0-dr), a, a, angle=90.0, fill=True)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.add_patch(rect)
ax.add_patch(circle1)
plt.axis('scaled')
plt.grid(True)
plt.savefig('output.png', dpi=400)
