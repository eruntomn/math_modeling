import numpy as np
from lab_3_task_1_constanta import g
from lab_3_task_1_constanta import post_planka as pl
from lab_3_task_1_constanta import post_bolcmana as bol1
from lab_3_task_1_constanta import cifra_elera as el


b = 30
h = 100
a = np.pi / 3
v = np.sqrt((h*g*(np.tan(b)**2)) / (2*(np.cos(a)**2)*(1 - np.tan(b)*np.tan(a))))
print(v)


t = 200
blb = 300
n = (2 / (np.sqrt(np.pi))) * (pl / (bol1 * t)**(3/2)) * (el ** ((-blb)/(bol1*t))) * (blb**(t / 2))
print(n)