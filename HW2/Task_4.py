guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    a = input('Гость пришел или ушел? ')
    if a.lower() == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    guest_name = input('Имя гостя: ')
    if a.lower() == 'пришел':
        if len(guests) < 6:
            print('Привет,', guest_name)
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    elif a.lower() == 'ушел':
        if guest_name in guests:
            print('Имя гостя:', guest_name)
            print('Пока,', guest_name)
            guests.remove(guest_name)
        else:
            print('Такого гостя нет')
    else:
        print('Неизвестная команда')