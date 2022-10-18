a = int(input())
if a % 4 != 0:
  print('год не високосный')
elif a % 100 == 0:
    if a % 400 == 0:
      print('год високосный')
    else:
      print('год не високосный')
else:
  print('год високосный')
      
      
  