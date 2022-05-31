import numpy as np
import proj_gd as gd
import utils
import matplotlib.pyplot as plt
import matplotlib.patches as mp

X = np.array([[2,0,0], [0,1,0]]).T
y = np.array([3,2,2])
t = 1

def f(w):
	return 0.5*np.sum((X@w - y)**2)

def fp(w):
	return X.T@(X@w - y)

# Implement the projection operator proj onto the l1 ball ||x||_1 <= t
#   START OF YOUR CODE
def proj(x):
	if np.linalg.norm(x,1)<1:
		return x
	k = x / np.abs(x)
	c = (t - k.T @ x) / (np.linalg.norm(k)**2)
	x = c * k + x
	return x
#   END OF YOUR CODE


w0 = np.array([-1,0.5])
stepsize = 0.1

w_traces, y_traces = gd.proj_gd(fp, proj, w0, stepsize=stepsize, tol=1e-8)

f_value = f(w_traces[-1])

print()
print('t = ', t)
print('number of iterations:', len(w_traces)-1)
print('solution:', w_traces[-1])
print('value:', f_value)

### visualization
Q = X.T@X
b = X.T@y
c = y@y

def f_2d(w1, w2):
	return 0.5 * Q[0,0] * w1**2 + 0.5 * Q[1,1] * w2**2 + Q[0,1] * w1 * w2 \
	       - b[0] * w1 - b[1] * w2 - 0.5 * c

def gap(w):
	return f(w) - f_value

path = '../figures/'
feasible_set = mp.Polygon([(-t,0), (0,t), (t,0), (0,-t)], alpha=0.5, color='y')
utils.plot_traces_2d(f_2d, w_traces, y_traces, feasible_set, path+f'lasso_traces_t{t}.pdf')
utils.plot(gap, w_traces, path+f'lasso_gap_t{t}.pdf')
