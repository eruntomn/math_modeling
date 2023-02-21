# Значения переменной величины взять в пределах ∈ [-5, 5], начальные значения изменяемых величин: y(0) = 3, dy(0)/dt = 0

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)

def div(sys, t):
    y, x = sys

    dydt = x
    dxdt = np.sin(x) + np.cos(x)

    return dydt, dxdt

y0 = 3
x0 = 0
sys0 = y0, x0

sol = odeint(div, sys0, t)

plt.plot(t, sol[:, 1], 'b')
plt.savefig('task_3.png')