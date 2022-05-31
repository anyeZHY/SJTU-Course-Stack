import numpy as np
import gd
import utils


X = np.array([
    [2, 0], [0, 1], [0, 0]
])
y = np.array([
    [3], [2], [2]
])

def f(w):
	return w.T @ X.T @ X @ w + y.T @ y - 2* y.T @ X @ w

def fp(w):
	return 2 * X.T @ X @ w - 2 * X.T @ y

x0 = np.array([[1.0], [1.0]])
stepsize = 0.2

x_traces = gd.gd_const_ss(fp, x0, stepsize=stepsize)

print(f'GD: stepsize={stepsize}, number of iterations={len(x_traces)-1}, solution = {x_traces[-1][0][0]}, {x_traces[-1][1][0]}')

s1 = np.linalg.solve(X[0:2], y.T[0][0:2])
print(f'np.linalg.solve: solution = {s1[0]}, {s1[1]}')
# utils.plot_traces_2d(f_2d, x_traces, f'../figures/gd_traces_gamma{gamma}_ss{stepsize}.pdf')
# utils.plot(f, x_traces, f'../figures/gd_f_gamma{gamma}_ss{stepsize}.pdf')
