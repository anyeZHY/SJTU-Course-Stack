import numpy as np
import LP
import matplotlib.pyplot as plt

## parameters of the standard form LP 
c =  np.array([-1, -3, 0, 0])
A =  np.array([
	[1, 1, 1, 0],
	[1, -2, 0, -1]
])
b =  np.array([
	[6],
	[-8]
])

x0 =  [2.0, 1.0, 3.0, 8.0]
x_traces = LP.barrier(c, A, b, x0)

print('')
for k,x in enumerate(x_traces):
	print('iteration %d: %s' % (k, x))
print('optimal value:', c@x_traces[-1])

### visualization
x12 = [x[0:2] for x in x_traces]
fig = plt.figure()
plt.plot([0,0, 4/3, 6,0], [0,4, 14/3, 0, 0], color='blue', linewidth=3)
line, = plt.plot(*zip(*x12), color='red', linewidth=3,  label='barrier method')
plt.scatter(*zip(*x12), color='red', marker='o', s=50)
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(handles=[line], fontsize=20)
plt.tight_layout()
fig.savefig('../figures/p2.pdf')


