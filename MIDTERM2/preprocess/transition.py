import numpy as np

# THIS FILE IS FOR PRODUCING THE TRANSITION MATRIX
A={}
Q = ['zeroaccess', 'winwebsec','zbot']
N = len(Q)

res = np.identity(N)
res += np.random.uniform(low=0., high=.25, size=(N, N))
res /=  res.sum(axis=1, keepdims=1)
print(type(res))
np.savetxt('transition_matrix', res)