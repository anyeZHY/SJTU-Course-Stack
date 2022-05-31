import numpy as np
import cvxpy as cp


x = cp.Variable((2,1))
# Form constraints
constraints = [cp.norm_inf(x) <= 1]
# Form objective.
A = np.array([
    [2, 1],
    [1, -3],
    [1, 2]
])
b = np.array([
    [5], [10], [-5]
])
obj = cp.Minimize(cp.norm1(A @ x - b))
# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value:", prob.value)
print("optimal var:","x1 =",x[0][0].value,"x2 =",x[1][0].value)
