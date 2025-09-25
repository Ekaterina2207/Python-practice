#s = v * t
#s(1 round) = 123
v = int(input('Введите скорость:'))
t = int(input('Введите время:'))
s = v * t
if v * t <= 123:
    print(s)
else:
    print(s - 123)