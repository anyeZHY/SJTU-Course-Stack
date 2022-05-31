import matplotlib.pyplot as plt
import numpy as np

plt.fill([3,20,100,5/3],[0,0,100,2/3],alpha=0.5)

x = np.arange(0,100,0.001)

b = np.arange(100)+23/12
for i in range(10):
    y = b[i] - 3 * x / 4
    plt.plot(x,y,'--')

plt.xlim([1,6])
plt.ylim([-0.03,2])
plt.scatter([5/3],[2/3],c='black')
# plt.show()
plt.savefig("../figures/p3.pdf")
