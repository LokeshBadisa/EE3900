import numpy as np
import matplotlib.pyplot as plt



N = 14

Y = np.loadtxt('simulation/codes/Y(k)real.dat')

#plots
plt.stem(range(0,N),Y)
plt.title('Filter Output using DFT')
plt.xlabel('$k$')
plt.ylabel('$Y(k)$')
plt.grid()# minor

#plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/yk.pdf')
#plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/yk.eps')

plt.show()