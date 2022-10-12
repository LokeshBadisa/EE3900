import numpy as np
from sympy import Sum,I,pi,exp
from sympy.abc import k
import matplotlib.pyplot as plt


def c(k):
    if k%2==0:
        return 2*A0/(np.pi * (1- k**2))
    else:
        return 0

def x(t):
    expr1 = Sum(c(k)*exp(2*I*pi*k*f0*t),(k,-float('inf'),float('inf')))
    return(expr1.doit())



A0 = 12
f0 = 50

t = np.linspace(0, 3/f0, 250)
plt.plot(t, np.abs(A0*np.sin(2*np.pi*f0*t)),label='$|A\sin{2\pi f_0t}|$')
plt.plot(t,x(t),label='$\sum_{k=-\infty}^{\infty}c_ke^{j2\pi kf_0t}$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.savefig('charger/figs/2.3.eps')
plt.savefig('charger/figs/2.3.pdf')
plt.show()

