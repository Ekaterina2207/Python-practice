#Создать классы для травоядного животного и травы. Животное должно уметь поедать траву,
#если испытывает голод, в противном случае отказываться от лакомства.
#Трава должна обладать питательностью, в зависимости от которой животное будет насыщаться.


class Grass:
    def __init__(self, food_value):
        self.food_value = max(1, food_value)
    def decrease_food_value(self, eaten_grass):
        self.food_value -= eaten_grass

class Cow:
    def __init__(self, satiety, max_satiety, name):
        self.satiety = max(0, satiety)
        self.max_satiety = max(self.satiety, max_satiety)
        self.name = name
    def eat_grass(self, grass: Grass):
        if grass.food_value == 0:
            print(f'Корова {self.name} говорит, что трава закончилась. Дайте другую траву.')
            return
        if self.satiety < self.max_satiety:
            eaten_grass = min(self.max_satiety - self.satiety, grass.food_value)
            self.satiety += eaten_grass
            grass.decrease_food_value(eaten_grass)
            print(f'Корова {self.name} съела {eaten_grass} травы.')
            print(f'Текущая сытость коровы {self.name} {self.satiety}.')
        else:
            print(f'Корова {self.name} сыта!')

small_grass = Grass(10)
middle_grass = Grass(50)
big_grass = Grass(100)
small_cow = Cow(5, 50, 'Милка')
big_cow = Cow(20, 200, 'Бурёнка')
small_cow.eat_grass(middle_grass)
big_cow.eat_grass(big_grass)
small_cow.eat_grass(small_grass)
big_cow.eat_grass(small_grass)
big_cow.eat_grass(small_grass)



