import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib as mpl



x = np.linspace(-5,5,100)
# constrains
y1 = 1 - 2*x
y2 = (1 - x) / 3
plt.plot(x,y1,label='bound-1')
plt.plot(x,y2,label='bound-2')

B = np.array([1,2])
ya = (0.6 - x)
plt.plot(x,ya,'g--',label='(a)')
yb = -x + 1
plt.plot(x,yb,'r--',label='(b)')
xc = np.zeros(100)
plt.plot(xc,y1,'k--',label='(c)')

for b in B:
    ya = (0.6 - x)+b
    plt.plot(x,ya,'g--')
    yb = -x + 1+b
    plt.plot(x,yb,'r--')
    xc = np.zeros(100)+b/2
    plt.plot(xc,y1,'k--')


plt.fill([0.4,1,2,2,0,0],[0.2,0,0,2,2,1],color='blue',alpha=.2)

plt.legend(loc='upper right')
plt.xlim(-0.1,1.5)
plt.ylim(0,1.5)
# plt.show()
plt.savefig('P2.pdf')
