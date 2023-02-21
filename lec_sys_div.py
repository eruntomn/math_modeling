# Системы диф. уравнений	
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(0, 10, 0.1)

# Опрделяем функцию для изменяемых величин
def diff_func(z, t): # z - изменяемая величина
    theta, omega = z

    # Первое уравнение системы
    dtheta_dt = omega
    # Второе уравнение системы
    domega_dt = - b * c * np.sin(theta)

    return dtheta_dt, domega_dt

# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
theta0 = np.pi - 0.1
omega0 = 0

# Начальное значение изменяемой величины системы
z0 = theta0, omega0

# Решаем систему диф. уравнений
b = 0.25
c = 5.0

sol = odeint(diff_func, z0, t)

# Строим решение в виде графика
plt.plot(t, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('sys_div.png')

# Строим решение в виде графика
plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')

plt.legend()
plt.savefig('2.png')