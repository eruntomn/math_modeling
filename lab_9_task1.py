import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 180, 1)

def bacteria(n, t):
    dnt = k * n
    return dnt

k = 1/10
n0 = 3

n_t = odeint(bacteria, n0, t)

plt.plot(t, n_t[:, 0], label='увеличение бактерий')
plt.xlabel('Время размножения')
plt.ylabel('Количество')
plt.title('Размножение бактерий')
plt.legend()
plt.savefig('1.png')

# Примерно через 60 секунд кол-во бактерий станет в 3 раза больше