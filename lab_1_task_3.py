
x = 3
#y = ((x**3)**0.5 / (x**3 + 3/x)) * (x**7*4 - x**5) + (80*(27*x**4 + 12*x**3 - 5*x**2 + 10)**0.5)
y1 = (x**3)**0.5 / (x**3 + 3/x)
y2 = 4*x**7 - x**5
y3 = y1 * y2
y6 = 80*(27*x**4 + 12*x**3 - 5*x**2 + 10)**0.5
y7 = y3 + y6

print(y7)

y8 = (16.7*4.32) // 1
y9 = 3 % 2 
y10 = y8 + y9
y11 = 31 % 12
y12 = (x**3.4) // 1
y13 = 14.5 + y11 - y12
y14 = (y10) / y13
print(y14)
