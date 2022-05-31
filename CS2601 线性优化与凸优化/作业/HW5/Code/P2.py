# import numpy as np
import cvxpy as cp

def solve(obj):
    prob = cp.Problem(obj, constraints)
    prob.solve()  # Returns the optimal value.
    print("status:", prob.status)
    print("optimal value:", prob.value)
    print("optimal var:","x1 =",x.value,", x2 =",y.value)

tmp = cp.Variable((2,1))
x = tmp[0][0]
y = tmp[1][0]
# Form constraints
constraints = [2*x + y >= 1,
               x + 3*y >= 1,
               x >= 0,
               y >= 0]
# Form objective.
obja = cp.Minimize(x+y)
objb = cp.Minimize(-x-y)
objc = cp.Minimize(x)
objd = cp.Minimize(cp.max(tmp))
obje = cp.Minimize(x**2+9*y**2)
# Form and solve problem.
print("------------(a)------------")
solve(obja)
print("------------(b)------------")
solve(objb)
print("------------(c)------------")
solve(objc)
print("------------(d)------------")
solve(objd)
print("------------(e)------------")
solve(obje)
