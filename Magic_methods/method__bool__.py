# Магический метод __bool__ Правдивость объектов в Pytho

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0

# задачки

# оздайте класс City, у которого есть:
#
# конструктор __init__, принимающий единственный аргумент - название города.
# Вам необходимо сохранить его в качестве атрибута экземпляра name, причем вам нужно преобразовать переданное имя города
# таким образом, чтобы первая буква каждого слова была заглавной,
# а остальные оказались строчными (пример "new york" - > "New York")
# переопределить метод __str__ таким образом, чтобы он возвращал имя города
# переопределить метод __bool__ так, чтобы он возвращал False ,
# если название города заканчивается на любую гласную букву латинского алфавита (a, e, i, o, u), в противном случае Tru

class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        if any((c in self.name[0]) for c in 'aeiou'):
            return False
        else:
            return True

# Сейчас вам нужно создать класс Quadrilateral (четырехугольник), в котором есть:
#
# конструктор __init__. Он должен сохранять в экземпляр класса два атрибута: width и height.
# При этом в сам метод __init__ может передаваться один аргумент(тогда в width и height присваивать это одно
# одинаковое значение, тем самым делать квадрат), либо два аргумента( первый идет в атрибут width, второй - в height)
# переопределить метод __str__ следующим образом:
# если width и height одинаковые, возвращать строку "Куб размером <width>х<height>
# в противном случае, возвращать строку "Прямоугольник размером <width>х<height>
# переопределить метод __bool__ так, чтобы он возвращал True, если объект является кубом, и False в противном случае

class Quadrilateral:

    def __init__(self, *args):
        self.width = args[0]
        self.height = args[-1]

    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height
