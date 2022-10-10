import numpy as np


n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
ca = np.cumsum(a)
if (np.allclose(ca[:98], a[2:] - 1)): print("1.1 correct")
else: print("1.1 incorrect")