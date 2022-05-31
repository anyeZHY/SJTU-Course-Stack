import numpy as np
import cvxpy as cp

w = cp.Variable((2,1))

X = np.array([
    [2, 0],
    [0, 1],
    [0, 0]
])
y = np.array([[3],[2],[2]])
# Constraints
t=1
for t in [1,100]:
    constraints = [
        cp.norm2(w)**2 <= t
    ]
    # Objective function
    obj = cp.Minimize(cp.norm2(X @ w - y)**2)
    # Solve problem.
    prob = cp.Problem(obj,constraints)
    prob.solve()  # Returns the optimal value.
    print("----------",t,"----------")
    print("status:", prob.status)
    print("optimal value:", prob.value)
    print("optimal var:","x1 =",w[0][0].value,"x2 =",w[1][0].value)
