import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

x = [0,4,4,0,0]
y = [4,4,-4,-4,4]


plt.fill_between(x,y,hatch="///",facecolor='grey')
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.set_xlabel('Re(s)',loc='right')
ax.set_ylabel('Im(s)',loc='top')
plt.setp(ax.get_yticklabels(), visible=False)
plt.xticks([0])
plt.title('ROC')
plt.savefig('../figs/2.4.eps')
plt.savefig('../figs/2.4.pdf')
subprocess.run(shlex.split("termux-open ../figs/2.4.pdf"))
#plt.show()