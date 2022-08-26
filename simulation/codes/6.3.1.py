import numpy as np
import matplotlib.pyplot as plt


N = 14

y = np.loadtxt('simulation/codes/ynreal.dat')
#plots
plt.stem(range(0,N),y)
plt.title('Filter Output using DFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

plt.show()
