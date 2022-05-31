import numpy as np
import newton
import utils
import matplotlib.pyplot as plt


def f(x):
	return f_2d(x[0], x[1])

def fp(x):
	#   START OF YOUR CODE
	x1 = x[0]
	x2 = x[1]
	gra1 = np.exp(x1+3*x2-0.1) + np.exp(x1 - 3*x2 - 0.1) - np.exp(-x1-0.1)
	gra2 = 3 * np.exp(x1+3*x2-0.1) - 3 * np.exp(x1 - 3*x2 - 0.1)
	return np.array([gra1, gra2])
	#	END OF YOUR CODE

def fpp(x):
	#   START OF YOUR CODE
	x1 = x[0]
	x2 = x[1]
	gra11 = np.exp(x1+3*x2-0.1) + np.exp(x1 - 3*x2 - 0.1) + np.exp(-x1-0.1)
	gra12 = 3 * np.exp(x1+3*x2-0.1) - 3 * np.exp(x1 - 3*x2 - 0.1)
	gra21 = 3 * np.exp(x1+3*x2-0.1) - 3 * np.exp(x1 - 3*x2 - 0.1)
	gra22 = 9 * np.exp(x1+3*x2-0.1) + 9 * np.exp(x1 - 3*x2 - 0.1)
	return np.array([
		[gra11, gra12],
		[gra21, gra22]
	])
	#	END OF YOUR CODE

def f_2d(x1, x2):
	return np.exp(x1+3*x2-0.1) + np.exp(x1 - 3*x2 - 0.1) + np.exp(-x1-0.1)

# use the value you find in HW7
f_opt = 2 * np.sqrt(2) * np.exp(-0.1)

def gap(x):
	return f(x) - f_opt

x0 = np.array([-1.5,1.0])
path = '/Users/anye_zhenhaoyu/Desktop/CS2601凸优化/作业/HW8/figures/'

#### Newton
x_traces = newton.newton(fp, fpp, x0)
f_value= f(x_traces[-1])


print()
print("Newton's method")
print('  number of iterations:', len(x_traces)-1)
print('  solution:', x_traces[-1])
print('  value:', f_value)

utils.plot_traces_2d(f_2d, x_traces, path+'nt_traces.pdf')
utils.plot(gap, x_traces, path+'nt_gap.pdf')
