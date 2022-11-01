#from - копирование
from lec_3_my_module import a,b

print(a*b)

# Копирование ВСЕХ атрибутов через * (так делать не надо)
from lec_3_my_module import *

print(c[2] * c[1])