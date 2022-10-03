import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20
y = np.zeros(20)


y[0] = x[0]
y[1] = -0.5*y[0]+x[1]

for n in range(2,k):
	if n < 6:
		y[n] = -0.5*y[n-1]+x[n]+x[n-2]
	elif n > 5 and n < 8:
		y[n] = -0.5*y[n-1]+x[n-2]
	else:
		y[n] = -0.5*y[n-1]

x=np.arange(0,k)
plt.plot(x,y,'o',markersize=12,label='Difference Equation')

N = 20
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,14), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)

H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)

Y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	Y[k] = X[k]*H[k]

y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		y[k]+=Y[n]*np.exp(1j*2*np.pi*n*k/N)

#print(X)
y = np.real(y)/N
x=np.arange(0,k+1)
plt.plot(x,y,'o',markersize=7,label='IDFT')

y=np.fft.ifft(Y)
y = np.real(y)
plt.plot(x,y,'o',markersize=3,label='IFFT')
plt.legend()
plt.savefig('simulation/figs/6.4.1.eps')
plt.show()