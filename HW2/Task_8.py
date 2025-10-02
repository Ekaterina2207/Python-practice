qty = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number}-й человек')
lst = list(range(1, qty+1))
index = 0
while len(lst) > 1:
    print('Текущий круг людей:', lst)
    index = ((index + number - 1) % len(lst))
    print('Выбывает человек под номером', index+1)
    lst.pop(index)
print('Остался человек под номером', lst[0])

# не получилось вывести строку "Начало счёта с номера...", т.к. начало счёта получается не с нужной цифры