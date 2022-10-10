import numpy as np
import matplotlib.pyplot as plt

n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
ca = np.cumsum(a)
k1=np.linspace(1,98,98)
plt.stem(k1,a[2:] - 1,label='$a_{n+2}-1$',markerfmt='o')
plt.stem(k1,ca[:98],label='$\sum_{k=1}^na_k$',markerfmt='o')
plt.legend()
plt.savefig('pingala/figs/1.1.eps')
plt.savefig('pingala/figs/1.1.pdf')
#plt.show()
if (np.allclose(ca[:98], a[2:] - 1)): print("1.1 correct")
else: print("1.1 incorrect")