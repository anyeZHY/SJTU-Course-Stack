import numpy as np

def solve(z,y):
    """
    compute lamda for a particular optimization problem:
    \min 0.5*\norm{x-z}^2
    s.t. y^Tx = 0
         x >= 0

    Inputs:
    - z: vector in objective function, of shape (N,) or (N,1)
    - y: vector in equality constraint function, of any given shape (N,) or (N,1)

    Returns a tuple of:
    - x: the optimal point of the problem, of shape (N,) or (N,1). x = (z-lamda*y)^+.
    - lamda: the Lagrange multiplier of the equality constraint function in KKT conditions.
    """

    shape = z.shape
    z = z.reshape(-1)
    y = y.reshape(-1)
    # initialize some parameters
    p = np.sum(y>0) # number of the elements > 0 in y
    m = len(y) - p
    u = np.sort(z[y==1]) # u = {z_i: i \in I_+}
    w = np.sort(-z[y==-1])
    u = np.append([-np.inf],u)
    u = np.append(u,[np.inf])
    w = np.append([-np.inf],w)
    w = np.append(w,[np.inf])

    U = np.zeros(p+1)
    W = np.zeros(m+1)
    for i in range(p):
        U[p-i-1] = U[p-i] + u[p-i]
    for i in range(m):
        W[i+1] = W[i] + w[i+1]
    # initialization of lamda, l and k
    lam = -1
    k = 0
    l = 0
    # Nlog(N) algortithm
    while (k<=p) and (l<=m):
        lam = (U[k] + W[l]) / (p - k + l)
        if (u[k] <= lam <= u[k+1]) and (w[l] <= lam <= w[l+1]):
            break
        if  u[k+1] < w[l+1]:
            k = k+1
        else:
            l = l+1
    return (((z - lam * y) > 0) * (z - lam * y)).reshape(shape), lam


z_p4 = np.array([1.0, 2.0, 1.0])
y_p4 = np.array([1.0, 1.0, -1.0])
x,lamda = solve(z_p4, y_p4)
print(x,lamda)
