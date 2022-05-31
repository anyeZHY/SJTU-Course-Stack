import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[4,4])
x=np.array([[1,3],[1,3]])
xlim=np.array([0,4])
mid=np.array([sum(x[0]),sum(x[1])])/2
k=(x[1][0]-x[1][1])/(x[0][0]-x[0][1])
k=-1/k
ylim=k*(xlim-mid[0])+mid[1]
plt.scatter(x[0],x[1])
plt.plot(xlim,ylim)
print(xlim,ylim,mid,k)
plt.xlim([0,4])
plt.ylim([0,4])
plt.arrow()
plt.show()
