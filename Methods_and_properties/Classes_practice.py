from math import sqrt
# Практика "Создание класса и его методов"

# класс Point(x, y)

class Point:

    list_points = []


    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x,new_y):
        self.x = new_x
        self.y = new_y

# внутри одного метода можно высывать метод другой

    def go_home(self):
        self.move_to(0, 0)

# написание такое го кода с таким синтаксисом называется dry тем самым мы убрали строчки которые у нас дублировались

# метод для удобного вывода

    def print_point(self):
        print(f'Точка с кардинатами ({self.x},{self.y})')

    def clc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Точка")

        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2 )