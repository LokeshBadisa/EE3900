import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex

x = [1, 1]
for i in range(23): x.append(x[-1] + x[-2])
y = np.add(x[:23], x[2:])
plt.stem(range(23), y)
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.tight_layout()
plt.savefig('/root/EE3900-Linear-Systems-and-Signal-Processing/pingala/figs/2.2.eps')
plt.savefig('/root/EE3900-Linear-Systems-and-Signal-Processing/pingala/figs/2.2.pdf')
subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))