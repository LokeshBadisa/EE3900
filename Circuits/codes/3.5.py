import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,1e-5,300)
y=(2/3)*(1+np.exp((-3/2)*1e6*x))
plt.plot(x,y,label='Theoretical')
plt.grid()
ax=plt.gca()
ax.set_xlabel('t')
ax.set_ylabel('$V_{C_0}(t)$')
simulation=np.loadtxt('3.5.dat')
data=[]
for i in range(0,int(1e6),10000):
    data.append(simulation[i])
data=np.array(data)
plt.scatter(data[:,0],data[:,1],label='Ngspice Simulation',color='orange')
plt.legend()
plt.savefig('../figs/3.5.1.eps')
plt.savefig('../figs/3.5.1.pdf')
plt.show()