#Упражнение 11

def digit_alpha_convert(num):
    try:
        num = int(num)
    except ValueError:
        raise ValueError
    if num < 0 or num > 100:
        raise ValueError
    elif num < 61:
        return str('F')
    elif num < 68:
        return str('E')
    elif num < 74:
        return str('D')
    elif num < 84:
        return str('C')
    elif num < 91:
        return str('B')
    elif num < 101:
        return str('A')


def alpha_digit_convert(letter):
    letter = letter.upper()
    if letter == 'A':
        return str('5')
    elif letter == 'B':
        return str('4')
    elif letter == 'C':
        return str('4-')
    elif letter == 'D':
        return str('3')
    elif letter == 'E':
        return str('3-')
    elif letter == 'F':
        return str('2')
    else:
        raise ValueError('Введено неверное значение')

print('Для выхода из программы нажмите Enter')
while True:
    grade = input('Введите Вашу оценку:')
    if grade == '':
        print('Выход из программы')
        break
    try:
        result = digit_alpha_convert(grade)
        print(f' Ваша оценка: {result}')
    except ValueError as error:
        try:
            result = alpha_digit_convert(grade)
            print(f' Ваша оценка: {result}')
        except ValueError as error:
            print(error)


