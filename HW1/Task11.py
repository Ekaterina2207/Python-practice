country = input('Введите название государства: ')
capital = input('Введите название столицы: ')
info = ("""
Государство - {country}, столица - {capital}
""")
print(
    info.format(
        country = country, capital = capital
    )
)