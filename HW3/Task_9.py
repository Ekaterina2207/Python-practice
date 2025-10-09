def decimal_system(a, b): #переводим введенное число в десятичную систему
    result = int(a, b)
    if b < 2 or b > 16:
        print('Ошибка ввода.')
    else:
        return result

def any_system(number, base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        return "0"
    result = ""
    is_negative = number < 0
    number = abs(number)
    while number > 0:
        result = alphabet[number % base] + result
        number //= base
    if is_negative:
        result = "-" + result
    return result

input_system = int(input('Введите основание исходной системы счисления (2, 8, 10 или 16): '))
integer = input('Введите число: ')
print(f'Число {integer} в десятичной системе счисления: {decimal_system(integer, input_system)}')
output_system = int(input('Введите основание целевой системы счисления (2, 8, 10 или 16): '))
print(f'Число {integer} в {output_system}-ой системе счисления: {any_system(decimal_system(integer, input_system), 
                                                                            output_system)}')