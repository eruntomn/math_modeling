import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 8, 0.1)

def diff_func(z, x): # z - изменяемая величина
    y, omega = z

    dydx = omega

    dset = omega * np.sin(y) - 3 * x * y - 5

    return dydx, dset

y0 =  0.01
omega0 = 0.05
z0 = y0, omega0

sol = odeint(diff_func, z0, x)

plt.plot(sol[:, 1], sol[:, 0], 'b')

plt.savefig('dddd.png')