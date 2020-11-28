from scipy.optimize import minimize, rosen, rosen_der
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: (x - 4) ** 2 + (x + 1) ** 2

fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
ax.plot(x, f(x))
plt.grid(True)
plt.show()

print('Nelder-Mead Method')
x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res1 = minimize(rosen, x0, method='Nelder-Mead', tol=1e-8, options={'disp':True})
print(res1.x)
print()

print('Powell\'s method')
res2 = minimize(rosen, x0, method='powell', tol=1e-8, options={'disp':True})
print(res2.x)
print()

print('Broyden–Fletcher–Goldfarb–Shanno Method')
res3 = minimize(rosen, x0, method='BFGS', tol=1e-8, jac=rosen_der, options={'disp':True})
print(res3.x)