import numpy as np
import matplotlib.pyplot as plt
import proj_gd as gd
from code_10 import solve
def svm(X,y):
	"""
	X: n x m matrix, X[i,:] is the m-D feature vector of the i-th sample
	y: n-D vector, y[i] is the label of the i-th sample, with values +1 or -1

	This function returns the primal and dual optimal solutions w^*, b^*, mu^*
	"""
	Xy = X * y
	Q = Xy @ Xy.T

	def fp(mu):
		# f(mu) = 0.5 * mu.T@Q@mu - np.sum(mu)
		return Q@mu - np.ones_like(mu)

	def proj(mu):
		# START OF YOUR CODE
		return solve(mu,y)[0]
		# return tmp
		# END OF YOUR CODE

	mu0 = np.zeros_like(y)
	mu_traces, _ = gd.proj_gd(fp, proj, mu0, stepsize=0.1, tol=1e-8)
	mu = mu_traces[-1]

	# recover the primal optimal solution from dual optimal solution
	# START OF YOUR CODE
	w = mu.T @ Xy
	N = len(mu[mu!=0]) # N may be 3.
	# print(X.shape,w.shape,y.shape)
	# print((y - X @ w.T))
	b = np.sum((y - X @ w.T)[mu!=0])/N
	# END OF YOUR CODE
	# print(w,b,mu)
	w = w.reshape(-1)
	return w, b, mu
