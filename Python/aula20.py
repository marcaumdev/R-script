import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-50, 60, 1, dtype=int)
y = -x**2+9*x-20

plt.plot(x,y)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('Função Quadrática')
plt.savefig('quadratica.eps', format='eps', dpi=600)
plt.show()