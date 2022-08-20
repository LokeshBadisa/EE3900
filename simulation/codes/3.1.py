import numpy as np
import matplotlib.pyplot as plt

x=np.loadtxt('xn.dat')

plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.xlabel('$n$')

plt.grid()
plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/3.1.pdf')
plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/3.1.eps')
plt.show()
