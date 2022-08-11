import numpy as np
import matplotlib.pyplot as plt


n=14
ynconv = np.loadtxt('codes/ynconv.dat')
nx=5
nh=n+2


#plots
plt.stem(range(0,nx+nh-1),ynconv)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()


plt.show()
