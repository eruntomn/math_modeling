import numpy as np
from lab_3_task_1_constanta import g

'''x0 = int(input())
vx0 = int(input())
y0 = int(input())
d = []

for t in range(0, 6):
  x = x0 + vx0 * t
  y = y0 + vx0 * t - (g * t ** 2) / 2
  
print(d)'''

x0 = int(input())
y0 = int(input())
v0x = int(input())
t = np.arange(0, 5, 0.01)
x = x0 + v0x * t
y = y0 + v0x * t - g * t ** 2 / 2

cords = np.zeros((len(t), 3))
for i in range(len(t)):
  cords[i, 0] = t[i]
  cords[i, 1] = x[i]
  cords[i, 2] = y[i]
print(cords)