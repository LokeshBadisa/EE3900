import numpy as np
import matplotlib.pyplot as plt

x=np.loadtxt('codes/xn.dat')
y=np.loadtxt('codes/yn.dat')
k=20

#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor


plt.show()
