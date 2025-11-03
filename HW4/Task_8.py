#Упражнение 8                       Свой элемент: Жизнь
#Вода + Воздух = Шторм              Жизнь + Вода = Рыба
#Вода + Огонь = Пар                 Жизнь + Земля = Червяк
#Вода + Земля = Грязь               Жизнь + Воздух = Птица
#Воздух + Огонь = Молния            Жизнь + Огонь = Лавамонстр
#Воздух + Земля = Пыль
#Огонь + Земля = Лава

#Классы основных элементов
class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Dirt()
        if isinstance(other, Live):
            return Fish()
        else:
            return None
    def __str__(self):
        return "Вода"
class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Live):
            return Bird()
        else:
            return None
    def __str__(self):
        return "Воздух"
class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Live):
            return Lavamonster()
        else:
            return None
    def __str__(self):
        return "Огонь"
class Earth:
    def __add__(self, other):
        if isinstance(other, Live):
            return Worm()
    def __str__(self):
        return "Земля"
class Live:
    def __str__(self):
        return "Жизнь"

#Классы элементов, получаемых путем сложения основных

class Storm:
    def __str__(self):
        return "Шторм"
class Steam:
    def __str__(self):
        return "Пар"
class Lightning:
    def __str__(self):
        return "Молния"
class Dirt:
    def __str__(self):
        return "Грязь"
class Dust:
    def __str__(self):
        return "Пыль"
class Lava:
    def __str__(self):
        return "Лава"
class Fish:
    def __str__(self):
        return "Рыба"
class Bird:
    def __str__(self):
        return "Птица"
class Lavamonster:
    def __str__(self):
        return "Лавамонстр"
class Worm:
    def __str__(self):
        return "Червяк"

water = Water()
air = Air()
fire = Fire()
earth = Earth()
live = Live()

print(f'Складываем {water} и {air}, получаем {water + air}')
print(f'Складываем {water} и {fire}, получаем {water + fire}')
print(f'Складываем {water} и {earth}, получаем {water + earth}')
print(f'Складываем {water} и {live}, получаем {water + live}')
print(f'Складываем {air} и {fire}, получаем {air + fire}')
print(f'Складываем {air} и {earth}, получаем {air + earth}')
print(f'Складываем {air} и {live}, получаем {air + live}')
print(f'Складываем {fire} и {earth}, получаем {fire + earth}')
print(f'Складываем {fire} и {live}, получаем {fire + live}')
print(f'Складываем {earth} и {live}, получаем {earth + live}')

