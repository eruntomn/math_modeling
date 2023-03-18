import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, y = z
    dv_xdt = k1 * (a - x - y)
    dv_ydt = k2 * (a - x - y)
    return dv_xdt, dv_ydt

a = 100
x_0 = 0
y_0 = 0
k1 = 0.1
k2 = 0.5
z0 = x_0, y_0

sol = odeint(move_func, z0, t)
plt.plot(t, sol[:, 0])
plt.plot(t, sol[:, 1])
plt.savefig('2.png')