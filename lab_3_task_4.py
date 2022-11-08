import numpy as np

M = 5
N = 4

A = np.zeros((M, N))

for m in range(M):
  for n in range(N):
    s = np.sin(N * (n+1) + M * (m + 1))
    if s > 0:
      A[m, n] = s
print(A)