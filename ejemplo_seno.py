'''
En este codigo se plotea la funcion Seno
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,15)
plt.plot(x, np.sin(x), 'o-')
plt.title('Diego Garcia sin tilde')
plt.savefig("Seno")
plt.show()
