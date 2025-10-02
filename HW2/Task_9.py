n = int(input('Введите количество друзей: '))
k = int(input('Введите количество долговых расписок: '))
balance = [0] * (n + 1)

for i in range(k):
    print(f'{i+1}-я расписка:')
    who = int(input('Кому?')) # Кто одолжил
    from_whom = int(input('От кого? ')) # У кого одолжили
    how_much = int(input('Сколько? ')) # Сумма
    balance[who] += how_much
    balance[from_whom] -= how_much
for i in range(1, n+1):
    print('Баланс друзей: ', balance[i])