#Создайте класс Point, экземпляры которого будут создаваться из координат x и y.
#Создайте класс прямоугольник — Rectangle. Метод __init__ принимает две точки — левый нижний и правый верхний угол.
#Каждая точка представлена экземпляром класса Point. Реализуйте методы вычисления площади и периметра прямоугольника.
#Добавьте в класс Rectangle метод contains. Метод принимает точку и возвращает True,
#если точка находится внутри прямоугольника и False в противном случае.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, left_low: Point, right_high: Point):
        self.left_low = left_low
        self.right_high = right_high
        self.check()
    def check(self):
        if self.left_low.y >= self.right_high.y or self.left_low.x >= self.right_high.x:
            raise ValueError('Координаты точки верхнего правого угла должны быть больше левого нижнего')
    def height(self):
        return self.right_high.y - self.left_low.y
    def width(self):
        return self.right_high.x - self.left_low.x
    def area(self):
        return abs(self.height() * self.width())
    def perimeter(self):
        return abs(2 * (self.height() + self.width()))
    def contains(self, point: Point):
        return ((self.left_low.x <= point.x <= self.right_high.x) and (self.left_low.y <= point.y <= self.right_high.y))

try:
    print('Введите координаты точки левого нижнего угла:')
    point_1 = Point(int(input()), int(input()))
    print('Введите координаты точки правого верхнего угла:')
    point_2 = Point(int(input()), int(input()))
    pr = Rectangle(point_1, point_2)
    print(f'Площадь прямоугольника равна: {pr.area()}')
    print(f'Периметр прямоугольника равен: {pr.perimeter()}')
    print('Введите координаты третьей точки:')
    point_3 = Point(int(input()), int(input()))
    is_inside = pr.contains(point_3)
    if is_inside:
        print('Ваша точка лежит в данном прямоугольнике.')
    else:
        print('Ваша точка не лежит в данном прямоугольнике.')
except Exception as error:
    print(error)
