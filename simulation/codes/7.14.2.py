import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

convolutiontime=np.loadtxt('simulation/codes/convolutiontime.dat')
dfttotaltime=np.loadtxt('simulation/codes/dfttime.dat')+np.loadtxt('simulation/codes/idfttime.dat')

print(dfttotaltime)
print(convolutiontime)
