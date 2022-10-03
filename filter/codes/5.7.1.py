import numpy as np
import matplotlib.pyplot as plt



k = 16

h = np.loadtxt('codes/hn.dat')

#subplots
plt.stem(range(0,k),h)
plt.title('Impulse Response Definition')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()# minor


plt.show()
