import numpy as np

def newton(fp, fpp, x0, tol=1e-5, maxiter=100000):
	"""
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	x0: initial point  
	tol: toleracne parameter in the stopping criterion. Newton's method stops 
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration
	"""
	x_traces = [np.array(x0)]
	x = np.array(x0)
	#   START OF YOUR CODE

	for i in range(maxiter):
		gradient = fp(x)
		Hes = fpp(x)
		# print(x)
		direction = np.linalg.inv(Hes) @ gradient
		if np.linalg.norm(direction)<tol:
			break
		x -= direction
		x_traces.append(np.array(x))

	#	END OF YOUR CODE

	return x_traces 

def damped_newton(f, fp, fpp, x0, alpha=0.5, beta=0.5, tol=1e-5, maxiter=100000):
	"""
	f: function that takes an input x an returns the value of f at x
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	x0: initial point in gradient descent
	alpha: parameter in Armijo's rule 
				f(x + t * d) > f(x) + t * alpha * <f'(x), d>
	beta: constant factor used in stepsize reduction
	tol: toleracne parameter in the stopping crieterion. Here we stop
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations in gradient descent.

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration and the total number of iterations in the inner loop
	"""
	x_traces = [np.array(x0)]
	stepsize_traces = []
	tot_num_iter = 0

	x = np.array(x0)

	for it in range(maxiter):
		#   START OF YOUR CODE
		
		gradient = fp(x)
		Hes = fpp(x)
		direction = -np.linalg.inv(Hes) @ gradient
		if np.linalg.norm(direction)<tol:
			break
		t = 1
		while f(x + t * direction) > f(x) + alpha * t * (fp(x).T @ direction):
			t = beta * t
		x += t * direction

		x_traces.append(np.array(x))
		stepsize_traces.append(t)
		tot_num_iter += 1

		#	END OF YOUR CODE

		x_traces.append(np.array(x))
		# stepsize_traces.append(stepsize)


	return x_traces, stepsize_traces, tot_num_iter
