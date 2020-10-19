import matplotlib.pyplot as plt
import numpy as np


plt.subplot()
x1 = np.linspace(1, np.exp(1), 100)
x2 = np.linspace(np.exp(1), 9, 100)
x3 = np.linspace(9, 12, 100)
plt.plot(x1, np.log(x1), 'r-')
plt.plot(x2, x2/np.exp(1), 'g--')
plt.plot(x3, 9*np.exp(1)**(8-x3), 'b-.')
plt.legend([r'$f(x) = ln(x)$', r'$y = x/e $', r'$y = 9*(e)^{8-x}$'])
plt.show()
