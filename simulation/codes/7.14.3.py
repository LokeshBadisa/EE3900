#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# In[24]:


convolutiontime=np.loadtxt('codes/timeforconvolution.dat')
df1=pd.DataFrame(convolutiontime)
xpoints1=df1[:][0]
ypoints1=df1[:][1]


# In[25]:


ffttime=np.loadtxt('codes/timeforfft.dat')
df=pd.DataFrame(ffttime)
xpoints2=df[:][0]
ypoints2=df[:][1]


# In[26]:


def objective1(x, a,b,c):
    return a * x**2 + c + b * x
popt, _ = curve_fit(objective1, xpoints1, ypoints1)
a,b,c=popt
print(a,b,c)


# In[27]:


def objective2(x, a):
    return a * x*np.log(x)
popt, _ = curve_fit(objective2, xpoints2, ypoints2)
a2=popt
print(a2)


# In[29]:


plt.scatter(xpoints1,ypoints1,s=10,label='Analytical Convolution')
plt.scatter(xpoints2,ypoints2,s=10,label='Analytical FFT&IFFT')
plt.plot(xpoints1,[a * x**2 + b * x +c for x in xpoints1],label='$y=x^2$')
plt.plot(xpoints2,[a2*x*np.log(x) for x in xpoints2],label='$y=xlogx$')
plt.legend()
plt.savefig('figs/time.eps')
plt.show()


# In[ ]:




