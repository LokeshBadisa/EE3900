import numpy as np
import matplotlib.pyplot as plt

n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
b_new = alpha**k + beta**k
print(b.size)
k1=np.linspace(1,99,99)
plt.stem(k1,b,label='$b_n$',markerfmt='o')
plt.stem(k1,b_new[:99],label='$ \u03B1 ^ n + \u03B2 ^ n $',markerfmt='o')
plt.legend()
plt.savefig('pingala/figs/1.3.eps')
plt.savefig('pingala/figs/1.3.pdf')
#plt.show()
if (np.allclose(b, b_new[:99])): print("1.3 correct")
else: print("1.3 incorrect")