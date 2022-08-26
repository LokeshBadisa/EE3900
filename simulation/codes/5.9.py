import numpy as np
from scipy import linalg

print(np.convolve([1,-0.5,1.25,-0.625,0.3125,-0.15625,0.078125],[1,2,3,4,2,1]))



h = np.array([1,-0.5,1.25,-0.625,0.3125,-0.15625])
x = np.array([1,2,3,4,2,1])
#x = np.reshape(x,6)
padding = np.zeros(h.shape[0] - 1, h.dtype)
first_col = np.r_[h, padding]
first_row = np.r_[h[0], padding]

H = linalg.toeplitz(first_col, first_row)

y = np.matmul(H,x)

#print(y)
for i in range(len(y)):
    print(y[i])
