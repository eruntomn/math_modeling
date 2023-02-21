# Значения переменной величины взять в пределах ∈ [-1, 1], начальные значения изменяемых величин: x(0) = -71, y(0) = 1, z(0) = -3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def div(sys, t):
    x, y, z = sys

    dxdt = 3 * x - y + z
    dydt = x + y + x
    dzdt = 4 * x - y + 4 * z
    return dxdt, dydt, dzdt

x0 = -71
y0 = 1
z0 = -3
sys0 = x0, y0, z0

sol = odeint(div, sys0, t)

plt.plot(t, sol[:, 1], 'b')
plt.savefig('task_dop_1.png')
