a = int(input())
b = int(input())
if a % b == 0:
  print(f'{a} делится на {b} без остатка. Частное равно:', a // b)
elif a % b != 0:
  print(f'{a} делится на {b} c остатком. Частное равно {a // b}, a остаток равен {a % b}')
elif b == 0:
  print('на 0 делить нельзя')
  

  