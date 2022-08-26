import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 20

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def h(n):
    if n == 0:
        return 1
    elif n > 0:
        return delta(n) + delta(n-2) - 0.5*h(n-1)
    else:
        return 2*(delta(n+1) + delta(n-1) - h(n+1))

def DFT(k, inp):
    ksum = 0
    for n in range(N):
        ksum += inp(n) * np.exp(-2j * np.pi * k * n / N)
    return ksum

def y(n):
    if n < 0:
        return 0
    else:
        return x(n) + x(n-2) - 0.5 * y(n-1)

def Y(k):
    return DFT(k, x) * DFT(k, h)

def IDFT(n, inp):
    nsum = 0
    for k in range(N):
        nsum += inp(k) * np.exp(2j * np.pi * k * n / N)
    return nsum / N

#FFT
x_vec = scipy.vectorize(x, otypes=[float])
h_vec = scipy.vectorize(h, otypes=[float])

n_arr = np.linspace(0, N-1, N)
x_arr = x_vec(n_arr)
h_arr = h_vec(n_arr)

X_arr = np.fft.fft(x_arr)
H_arr = np.fft.fft(h_arr)
Y_arr = X_arr * H_arr
y_arr = np.fft.ifft(Y_arr)

#Difference Equation
N2 = np.linspace(0, 19, 20)
vec_y = scipy.vectorize(y, otypes=[float])

#DFT
nvalues = np.linspace(0, N-1, N)
#print(type(nvalues))


plt.scatter(nvalues, (np.real(IDFT(nvalues, Y))).tolist(),color='r',label='IDFT')
plt.scatter(n_arr, (np.real(y_arr)).tolist(),color='g',label='IFFT')
plt.scatter(N2, (vec_y(N2)).tolist(),color='b',label='Difference Equation')


#Graph labelling
plt.legend()
plt.title('Filter Output using various methods')
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.grid()
#plt.savefig('simulation/figs/6.4.png')
plt.show()




