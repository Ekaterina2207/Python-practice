from math import cbrt

x = int(input('Введите значение числа x: '))
y = int(input('Введите значение числа y: '))
z = int(input('Введите значение числа z: '))
print(round((cbrt((x**5 + 7)/(abs(-6)*y)))/7-z%y, 3))