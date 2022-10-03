import numpy as np
import matplotlib.pyplot as plt



N = 20


#print(X), (H)
X = np.loadtxt('simulation/codes/X(k)real.dat')
H = np.loadtxt('simulation/codes/H(k)real.dat')

#subplots
plt.subplot(2,1,1)
plt.stem(range(0,N),X)
plt.title('')
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.grid()# minor

plt.subplot(2,1,2)
plt.stem(range(0,N),H)
plt.title('')
plt.xlabel('$k$')
plt.ylabel('$H(k)$')
plt.grid()# minor
'''
plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/xkhk.pdf')
plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/xkhk.eps')
''' 
plt.show()   


