import numpy as np
import cvxpy as cp

w = cp.Variable((5,1))
x1 = w[0][0]
x2 = w[1][0]
t1 = w[2][0]
t2 = w[3][0]
t3 = w[4][0]

n = 2
m = 3
AA = np.array([
    [2, 1],
    [1, -3],
    [1, 2]
])
bb = np.array([
    [5], [10], [-5]
])
En = np.eye(n)
Em = np.eye(m)
O = np.zeros((n,m))
A1 = np.append(En,O,axis=1)
A2 = np.append(-En,O,axis=1)
A3 = np.append(AA,-Em,axis=1)
A4 = np.append(-AA,-Em,axis=1)
A = np.concatenate((A1,A2,A3,A4),axis=0)
b = np.concatenate((np.ones((n,1)),np.ones((n,1)),bb,-bb),axis=0)
c = np.concatenate((np.zeros((n,1)),np.ones((m,1))),axis=0)
# print(A,b,c)
# Form and solve problem.
prob = cp.Problem(cp.Minimize(c.T@w),
                 [A @ w <= b])
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value:", prob.value)
print("optimal var:","x1 =",w[0][0].value,"x2 =",w[1][0].value,
      "t1 =",w[2][0].value,"t2 =",w[3][0].value,"t3 =",w[4][0].value)
