import numpy as np
'''from random import randint
a = np.zeros((4, 3))
b = np.zeros((4, 3))
c = np.zeros((4, 3))
for i in range(4):
  for j in range(3):
    a[i, j] = randint(0, 100)
    b[i, j] = randint(0, 100)
print(a)
print(b)
for g in a:
  for k in b:
    if g > k:
      c += g
    else:
      c += k'''
      
mx = 0
for n in a:
  if n > mx:
    mx = n
print(mx)

A = np.zeros((M, N))

for m in range(M):
  for n in range(N):
    s = np.sin(N * (n+1) + M * (m + 1))
    if s > 0:
      A[m, n] = s
print(A)
