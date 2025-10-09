print('Загадайте число от 1 до 100 ')
print('Гарантированно угадаю за семь попыток или меньше ')
low = 1
high = 100
attempt_number = 0
while low <= high:
    mid = (high + low) // 2
    attempt_number += 1
    answer = int(input(f'Попытка №{attempt_number}: Ваше число 1-равно, 2-больше или 3-меньше, чем {mid}? '))
    if answer == 1:
        print(f'Ваше число = {mid}. Угадано за {attempt_number} попыток.')
        break
    elif answer == 2:
        low = mid + 1
    elif answer == 3:
        high = mid - 1





