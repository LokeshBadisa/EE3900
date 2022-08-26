import numpy as np
import matplotlib.pyplot as plt

#x=np.loadtxt('simulation/codes/xn.dat')
y=np.loadtxt('simulation/codes/yn.dat')
k=14
'''
#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,22),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()# minor


#plt.subplot(2, 1, 2)'''
plt.xticks(np.arange(0,14,1))

#plt.savefig('simulation/figs/ynconv2.pdf')
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
plt.savefig('simulation/figs/ynconv2.png')
plt.show()

