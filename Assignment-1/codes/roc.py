
import numpy as np
import matplotlib.pyplot as plt

x = [4,-4,-4,4,4]
y = [4,4,-4,-4,4]


plt.fill_between(x,y,hatch="///",facecolor='grey')
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.title('ROC')
plt.savefig('Assignment-1/figs/roc.eps')
plt.savefig('Assignment-1/figs/roc.pdf')
plt.show()