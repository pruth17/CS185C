import init
import json
import numpy as np
divider="*****************************"

pi=init.initial_state
v=init.values

A=[]
B={}

T=30
N=v["N"]
V=v["V"]
M=v["M"]
Q=v["Q"]
O="918273734856HJWUERNM"


print(divider, "MAP OF OBSERVATION SYMBOLS", divider)
for i in range(M):
  print(V[i], ":-",init.observation_symbols[i])

# OBSERVATION MATRIX
print(divider, "POPULATING OBSERVATION MATRIX", divider)    
with open('observation_matrix') as json_file:
  B = json.load(json_file)

print("N x M =", N, "x", M, "=", N*M)

# TRANSITION MATRIX
print(divider, "POPULATING TRANSITION MATRIX", divider)    
A = np.loadtxt('transition_matrix')
  
print("N x N =", N, "x", N, "=", N*N)