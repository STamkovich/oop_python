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

# задачки

#    Создайте класс Dog, у которого есть:
# конструктор __init__, принимающий 2 аргумента: name, age.
# метод description, который возвращает строку в виде "<name> is <age> years old"
# метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";

class Dog:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Ваша задача реализовать класс Stack, у которого есть:
#
# метод __init__  создаёт новый пустой стек. Параметры данный метод не принимает. Создает атрибут экземпляра values,
# где будут в дальнейшем хранятся элементы стека в виде списка (list),
# изначально при инициализации задайте значение атрибуту values равное пустому списку;
# метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает.
# метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. Стек изменяется.
# Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";
# метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется.
# Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;
# метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
# метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.

class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")

        else:
            return self.values.pop(-1)


    def peek(self):
        if len(self.values) == 0:
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

