#Описать класс десятичного счётчика. Он должен обладать внутренней переменной, хранящей текущее значение,
#методами повышения значения (increment) и понижения (decrement), получения текущего значения get_counter.
#Учесть, что счётчик не может опускаться ниже 0.

class Counter:
    def __init__(self):
        self.__count = 0
    def increment(self):
        self.__count += 1
    def decrement(self):
        if self.__count < 1:
            raise ValueError('Stop')
        self.__count -= 1
    def get_counter(self):
        return self.__count

counter = Counter()
counter.increment()
counter.increment()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.decrement()
print(counter.get_counter())