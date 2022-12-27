import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()  # Создание пространства и подпронстранства
anim_object, = plt.plot([], [], '-', lw = 2)  # Объект анимации

xdata, ydata = [], []  # Координаты объекта анимации

ax.set_xlim(0, 2*np.pi)  # Пределы изменения переменной X
ax.set_ylim(-1, 1)  # Пределы изменения переменной Y

def update(frame):  # Функция подстановки координат в объект анимации
    xdata.append(frame)  # Расcчет координаты X
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)  # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Cтандартный вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100 # Интервал между кадрами
                                 # По умолчанию 200 милисекунд
                    )
ani.save('pic_funanim.png')
