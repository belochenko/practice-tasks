import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spopt

f = lambda x: (x - 3) ** 2 + (x + 5) ** 2

fig, ax = plt.subplots()
p = np.linspace(-10, 10, 100)
ax.plot(p, f(p))
x_min1 = spopt.fmin_bfgs(f, -10)

print(x_min1)  # 1
print(spopt.brent(f))  # 2
print(spopt.fminbound(f, -10, 10))  # 3

fig.show()
