import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# h = v0*t + g*t**2/2

R = 640000
h = 50 * R
r = np.arange(h+R, R, -1000)


def move_meteor(v, r):
    dvdr = - G * M / (v * r ** 2)
    return dvdr

G = 6.67 * 10 ** (-11)
M = 5.9 * 10**24
v0 = 10

v_r = odeint(move_meteor, v0, r)

plt.plot(r, v_r[:, 0], label='траектория')
plt.xlabel('Время')
plt.ylabel('Высота')
plt.title('Падения метеорита')
plt.legend()
plt.savefig('meteor.png')