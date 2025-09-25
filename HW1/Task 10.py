team = input('Введите название футбольной команды: ')
info = '- чемпион!'
print(team, info)
print('-' * len(team))
team = team.lower()
info = ("""
Количество символов в названии команды: {symbols}
Есть ли буква 'п' в названии команды: {letter_p}
Количество букв 'а' в названии команды: {letter_a}
""")
print(
    info.format(
        symbols = len(team),
        letter_p = 'п' in team,
        letter_a = team.count('а')
    )
)

