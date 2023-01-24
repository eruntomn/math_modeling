import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 10**6, 100)

# Запись диф. уравнения в виде функции
def radio_function(m, t):
    dmdt = - k * m
    return dmdt

# Определение начальных условий и параметров
m_0 = 10
k = 1.61 * 10 ** (-6) # Постоянная распада для Висмута 210

# Решение диф. уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)

# Посмтроение графика 
plt.plot(t, m_t[:, 0], label='Распад Висмута')
plt.xlabel('период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()
plt.savefig('0.png')