import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(0,1,25)
#x2=np.linspace(0,1,25)
y1=np.full(len(x),5)
y2=np.full(len(x),4.985)
y3=np.full(len(x),4.989)
plt.grid()
plt.plot(x,y1,label='Analytical')
plt.scatter(x,y2,color='red',label='Butterworth')
plt.scatter(x,y3,color='orange',label='Chebyshev')
plt.xlabel('Time(s)')
plt.ylabel('Voltage(V)')
plt.legend()
plt.savefig('../figs/original.pdf')
plt.savefig('../figs/original.eps')
