import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,11,2)
y = np.zeros(len(x))




plt.stem(-1,1)
plt.stem(x,y)
plt.xlabel('n')
plt.xticks(np.arange(-10,11,2))
plt.ylabel('x(n)')
plt.title('$\delta[n+1]$')
plt.yticks(np.arange(0,2.5,0.5))
plt.savefig('Assignment-1/figs/unitsample.eps')
plt.savefig('Assignment-1/figs/unitsample.pdf')
plt.show()