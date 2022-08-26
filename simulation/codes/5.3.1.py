import numpy as np
import matplotlib.pyplot as plt


hn = np.loadtxt('simulation/codes/hn.dat')

plt.stem(np.arange(16), hn)
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()


plt.show()





