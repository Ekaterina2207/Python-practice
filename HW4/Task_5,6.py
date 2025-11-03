#Упражнение 5-6.
#Создать класс для часов. Должна быть возможность установить время при создании объекта.
#Также необходимо реализовать методы, с помощью которых можно добавлять по одной минуте/секунде
#или по одному часу к текущему времени. Помнить, что значения минут и секунд не могут превышать 59, а часов 23.
#Доработать предыдущую задачу, чтобы можно было складывать двое часов друг с другом.
#Для перегрузки оператора + использовать метод __add__(self, other).

class Clock:
    def __init__(self, hh, mm, ss):
        if not (0 <= hh < 24):
            raise ValueError("Часы должны быть от 0 до 23")
        if not (0 <= mm < 59):
            raise ValueError("Минуты должны быть от 0 до 59")
        if not (0 <= ss < 59):
            raise ValueError("Секунды должны быть от 0 до 59")
        self.hh = hh
        self.mm = mm
        self.ss = ss
    def hour(self):
        self.hh = (self.hh + 1) % 24
    def minute(self):
        self.mm += 1
        if self.mm >= 60:
            self.mm = 0
            self.hour()
    def second(self):
        self.ss += 1
        if self.ss >= 60:
            self.ss = 0
            self.minute()
    def __str__(self):
        return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}"
    def __add__(self, other):
        new_ss = 0
        new_mm = 0
        new_hh = 0
        if self.ss + other.ss > 59:
            new_mm += 1
        new_ss += (self.ss + other.ss) % 60
        if self.mm + other.mm > 59:
            new_hh += 1
        new_mm += (self.mm + other.mm) % 60
        new_hh = (self.hh + other.hh + new_hh) % 24
        return Clock(new_hh, new_mm, new_ss)

clock = Clock(23, 31, 31)
clock_2 = Clock(2, 30, 31)
clock.minute()
clock.second()
print(clock)
print(clock_2)
total_clock = clock_2 + clock
print(total_clock)
