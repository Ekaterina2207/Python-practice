lst_1 = []
for i in range(3):
    digit_1 = int(input(f'Введите {i+1}-е число для первого списка: '))
    lst_1.append(digit_1)
lst_2 = []
for i in range(7):
    digit_2 = int(input(f'Введите {i+1}-е число для второго списка: '))
    lst_2.append(digit_2)
print(lst_1)
print(lst_2)
lst_1.extend(lst_2)
print('Новый первый список с уникальными элементами:', list(set(lst_1)))