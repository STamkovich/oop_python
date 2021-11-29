# 3.8 Полиморфизм в Python
# полиморфизм относиться к трём основным базовым понятиям ООП вне зависимости на каком языке вы пишите
# полиморфизм -  это возможнасть обраюотки разных объектов путём использования одного и того же метода по названию
class Restangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Restangle {self.a} x {self.b} = {self.a * self.b}'

    # def get_rect_area(self):# был ранее
    def get_area(self):
        return self.a * self.b


class Square:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a} ** 2 = {self.a ** 2}'

    # def get_sq_area(self):# был ранее
    def get_area(self):
        return self.a ** 2


class Cirkle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Cirkle r = {3.14 * self.r ** 2}'

    # def get_cir_area(self):# был ранее
    def get_area(self):
        return 3.14 * self.r ** 2


# ______________________________________________________

# Полиморфизм
from Polymorfizm import Restangle, Square, Cirkle

a = Restangle(2, 4)
b = Restangle(4, 9)
# print(a.get_rect_area(), b.get_rect_area())# 8 36
print(a.get_area(), b.get_area())  # 8 36
c1 = Square(5)
c2 = Square(8)
# print(c1.get_sq_area(), c2.get_sq_area())# 25 64
print(c1.get_area(), c2.get_area())  # 25 64
cir1 = Cirkle(9)
cir2 = Cirkle(4)
# print(cir1.get_cir_area(), cir2.get_cir_area())# 254.34 50.24
print(cir1.get_area(), cir2.get_area())  # 254.34 50.24
figures = [a, b, c1, c2, cir1, cir2]
for figure in figures:
    # if isinstance(figure, Square):
    #    print(figure.get_sq_area())
    # elif isinstance(figure, Cirkle):
    #    print(figure.get_cir_area())
    # else:
    #    print(figure.get_rect_area())
    print(figure.get_area())
print(a)
print(b)
print(c1)
print(c2)
print(cir1)
print(cir2)
