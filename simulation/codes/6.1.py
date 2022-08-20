import numpy as np
import matplotlib.pyplot as plt



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


#print(X), (H)
X = np.real(X)/N
H = np.real(H)/N

#subplots
plt.subplot(2,1,1)
plt.stem(range(0,N),X)
plt.title('')
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.grid()# minor

plt.subplot(2,1,2)
plt.stem(range(0,N),H)
plt.title('')
plt.xlabel('$k$')
plt.ylabel('$H(k)$')
plt.grid()# minor

plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/xkhk.pdf')
plt.savefig('/home/lokesh/Desktop/BTech/EE3900-Linear-Systems-and-Signal-Processing/figs/xkhk.eps')

plt.show()    


