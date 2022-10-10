import numpy as np
import matplotlib.pyplot as plt
n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
t = 10**k
ta = a*(1/t)
eps = 1e-6
ans = 10/89
sa = np.cumsum(ta)
plt.stem(k,sa,label='Simulation')
plt.axhline(y=10/89,color='r',label='Theoretical')
plt.legend()
plt.savefig('pingala/figs/1.2.eps')
plt.savefig('pingala/figs/1.2.pdf')
#plt.show()
if (abs(sa[-1] - ans) < eps): print("1.2 correct")
else: print("1.2 incorrect")