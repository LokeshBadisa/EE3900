import numpy as np
from sympy import Sum,pi,sin,cos
from sympy.abc import k
import matplotlib.pyplot as plt


def a(k):
    if k==0:
        return 2*A0/pi
    if k%2==0:
        return 4*A0/(pi * (1- k**2))
    else:
        return 0

def b(k): 
    return 0

def x(t):
    expr1 = Sum(a(k)*sin(2*pi*k*f0*t)+b(k)*cos(2*pi*k*f0*t),(-float('inf'),float('inf')))
    return(expr1.doit())



A0=12
f0=50

t=np.linspace(0,3/(f0),250)
plt.plot(t, np.abs(A0*np.sin(2*np.pi*f0*t)),label='$|A\sin{2\pi f_0t}|$')
plt.scatter(t,x(t),color='orange',label='$\sum_{k=0}^\infty(a_k\cos2\pi kf_0t+b_k\sin2\pi kf_0t)$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.savefig('charger/figs/2.6.eps')
plt.savefig('charger/figs/2.6.pdf')
#plt.show()

