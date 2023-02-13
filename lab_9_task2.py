import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Инвестируемый объём в данный момент времени * коэффицент = - скорость * время
# - k * id = t * i0

t = np.arange(0, 20, 0.1)
def investizia(t, i):
    d = (k / np.pi) * e0* s* np.cos(np.pi/12*(t-12))
    return d

k = 0.08
i0 = 1000
i_t = odeint(investizia, i0, t)


plt.plot(t, i_t[:, 0], label='Инвестиции')
plt.xlabel('Количество лет')
plt.ylabel('Инвестиции')
plt.title('Вклад')
plt.legend()
plt.savefig('2.png')