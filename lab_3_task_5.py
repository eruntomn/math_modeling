import numpy as np

M = 4
N = 5

A = np.zeros((M, N))

for m in range(M):
  for n in range(N):
    s = np.sin(N * (n+1) + M * (m + 1))
    if s > 0:
      A[m, n] = s
print(A)

c = np.zeros((M, N))
for i in range(M):
  for j in range(N):
    '''c[i, j] = A[i, j]
A[:, 2], c[:, 3] = c[:, 3], A[:, 2]'''
    
print(A)
