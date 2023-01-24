import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 10, 0.1)

def mat_move(t, v):
    d = g - (y / m * v**2)
    # g - ускорение свободного падения, y - коэффицент сопротивления
    return d

g = 10
m = 2 
v = 15
y = 0.295

d_t = odeint(mat_move, m, t)

plt.plot(t, d_t[:, 0], label='линия')
plt.xlabel('Сила сопротивления')
plt.ylabel('Сила')
plt.title('Сила Сибири')
plt.legend()
plt.savefig('3.png')