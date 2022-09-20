import numpy as np
import matplotlib.pyplot as plt
x = [0.7,-0.7,-0.7,0.7,0.7]
y = [0.7,0.7,-0.7,-0.7,0.7]
x1=np.arange(0,2*np.pi,0.01)
X1=0.5*np.cos(x1)
Y1=0.5*np.sin(x1)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.set_xlabel('Re(z)',loc='right')
ax.set_ylabel('Im(z)',loc='top')
plt.plot(X1,Y1)
plt.xticks(np.arange(-0.5,0.6,0.1))
plt.yticks(np.arange(-0.5,0.6,0.1))
plt.fill_between(X1,Y1,y)
plt.title('ROC')
plt.savefig('roc1.eps')
plt.savefig('roc1.pdf')
plt.show()