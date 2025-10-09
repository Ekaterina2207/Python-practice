def magic_date(day, month, year ):
    year = year%100
    return day*month == year

day = int(input('Введите число в формате ДД: '))
month = int(input('Введите месяц в формате ММ: '))
year = int(input('Введите год в формате ГГГГ: '))
if magic_date(day, month, year):
    print('Магическая дата')
else:
    print('Дата не магическая')

#магические даты 20 века
def valid_date(dd, mm, yyyy):
    if mm > 12 or dd > 31:
        return False
    is_leapyear = (yyyy % 4 == 0 and yyyy % 100 != 0) or yyyy % 400 == 0
    monthdays = [31, 28 + is_leapyear, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dd <= monthdays[mm - 1]

print('Выведем список магических дат ХХ века:')
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        for day in range(1, 32):
            if valid_date(day, month, year):
                if magic_date(day, month, year):
                    print(f'{day}.{month}.{year}')