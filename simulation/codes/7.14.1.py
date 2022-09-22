import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

convolutiontime=np.loadtxt('codes/convolutiontime.dat')
directdft=np.loadtxt('codes/dfttime.dat')+np.loadtxt('codes/idfttime.dat')
fftct=np.loadtxt('codes/totalffttimect.dat')
fftmat=np.loadtxt('codes/fftmat.dat')
data=[convolutiontime,directdft,fftct,fftmat]
for i in range(0,len(data)):
    data[i]*=1e6

methods = ['Convolution','Direct DFT and IDFT','FFT through Cooley-Tukey & IFFT through Conjugate','FFt through Matrix Decomposition']
df=pd.DataFrame(data,methods)
time = [convolutiontime,directdft,fftct,fftmat]
print(df)
plt.bar(df.index,df[0])
plt.ylabel('Time in $\mu$s')
plt.xlabel('Method Employed')
plt.savefig('figs/TimeComparison.eps')
plt.show()

