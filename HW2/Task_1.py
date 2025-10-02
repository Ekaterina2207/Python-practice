a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
total_5 = 0
total_3 = 0
a.extend(b)
for i in a:
    if i == 5:
        total_5 += 1
print('Количество цифр 5:', total_5)
while 5 in a:
    a.remove(5)
a.extend(c)
for i in a:
    if i == 3:
        total_3 += 1
print('Количество цифр 3:', total_3)
print('Итоговый список:', a)
