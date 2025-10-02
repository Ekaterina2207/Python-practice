lst_skates = [] #список размеров коньков
n = int(input('Введите количество коньков: '))
for i in range(n):
    size_skates = int(input(f'Введите размер {i+1}-й пары: '))
    lst_skates.append(size_skates)
lst_feet = [] #список размеров ног
people = int(input('Введите количество людей: '))
for j in range(people):
    size_feet = int(input(f'Введите размер ноги {j+1}-го человека: '))
    lst_feet.append(size_feet)
lst_feet.sort()
lst_skates.sort()
max_qty = 0 #переменная для подсчета максимального количества людей на роликах
i = 0
j = 0
while i < len(lst_skates) and j < len(lst_feet):
    if lst_skates[i] >= lst_feet[j]:
        max_qty += 1
        i += 1
        j += 1
    else:
        i += 1

print('Наибольшее кол-во людей, которые могут взять ролики:', max_qty)
