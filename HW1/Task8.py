a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
info = ("""
Наименьшее число = {mn}
Среднее число = {srednee}
Наибольшее число = {mx}
""")
print(
    info.format(
        mn = min(a, b, c),
        srednee = (a + b + c) - min(a, b, c) - max(a, b, c),
        mx = max(a, b, c)
    )
)