# Slots - ограничение атрибутов
# при использовании slots ваши объекты занимают меньше место по памяти
# при помощи данной конструкции вы можете экземплярам вашего класса  передать только определённые атрибуты
# у класса у которого есть Slots операции над объектами будут выполняться гораздо быстрее(обращение создание, удаление)
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', "y")  # перечисление отрибутов которые будут использованы в нашем классе

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
print(s.__sizeof__(), s.__dict__.__sizeof__())
s1 = PointSlots(3, 4)
print(s1.__sizeof__())  # сдесь же уже общий объём всего занятого пространства нашег объекта


# переменная dict пропадёт
# можно изменять  значения атрибутов но нельзя добавлять новые атрибуты
# можно удалять атрибуты но при этом этот же атрибут опять можно будет потом создать

# 4.8 Slots: свойства(property) и наследования

class Restangle:
    __slots__ = 'weidth', 'heigth'

    def __init__(self, a, b):
        self.weidth = a
        self.heigth = b

    @property
    def perimetr(self):
        return (self.weidth + self.heigth) * 2

    @property
    def area(self):
        return self.weidth * self.heigth


b = Restangle(4, 5)
print(b.area)
print(b.perimetr)


class Restangle:
    __slots__ = '__weidth', 'heigth'

    def __init__(self, a, b):
        self.weidth = a
        self.heigth = b

    @property
    def weidth(self):
        return self.__weidth

    @weidth.setter
    def weidth(self, value):
        print('setter called')
        self.__weidth = value


class Square(Restangle):
    pass


c = Square(4, 5)  # setter called
print(c.weidth)  # 4
print(c.__dict__)  # {}
c.zz = 200
print(c.zz)  # 200


class Restangle:
    __slots__ = '__weidth', 'heigth'

    def __init__(self, a, b):
        self.weidth = a
        self.heigth = b

    @property
    def weidth(self):
        return self.__weidth

    @weidth.setter
    def weidth(self, value):
        print('setter called')
        self.__weidth = value


class Square(Restangle):
    __slots__ = 'color'

    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color


c = Square(4, 5, 'Red')  # setter called
print(c.weidth, c.heigth, c.color)  # 4 5 Red


# Новые атрибуты не присвоить
class Restangle:
    __slots__ = '__weidth', 'heigth'

    def __init__(self, a, b):
        self.weidth = a
        self.heigth = b

    @property
    def weidth(self):
        return self.__weidth

    @weidth.setter
    def weidth(self, value):
        print('setter called')
        self.__weidth = value


class Square(Restangle):
    __slots__ = tuple()

    def __init__(self, a, b):
        super().__init__(a, b)


c = Square(4, 5)  # setter called
print(c.weidth, c.heigth)  # 4 5
# Новые атрибуты не присвоить. При вызове __dict__ будет ошибка.
