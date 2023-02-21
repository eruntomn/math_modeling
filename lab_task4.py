# Значения переменной величины взять в пределах ∈ [-5, 5], начальные значения изменяемых величин: y(0) = 4, dy(0)/dt = -1

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)

def div(sys, t):
    y, x = sys

    dydt = x
    dxdt = - 4 * x - 5 * y

    return dydt, dxdt

y0 = 4
x0 = -1
sys0 = y0, x0

sol = odeint(div, sys0, t)

plt.plot(t, sol[:, 0], 'b')
plt.savefig('task_4.png')