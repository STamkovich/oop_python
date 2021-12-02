# 4.3 Переопределение методов в Python
#  Класс Person наследуется от объекта

class Person:

    def __init__(self, name):
        # print('init Person')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек ходит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()  # внутри одного метода можно вызывать другие методы
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'


# переопределить родительский метод это означает внутри дочернего класса создать такой же метод(с таким же названием)
# и внутри его определить другое поведение
# так же можно переопределять атрибуты
# так же можно переопределять и методы

class Doctor(Person):
    name = 'Ivan'

    def breathe(self):
        print('Доктор дышит')

    def walk(self):
        print('Доктор ходит')

    def sleep(self):
        print('Доктор спит')

    def __str__(self):
        return f'Doctor {self.name}'


d = Doctor('John')
p = Person('Adam')
p.combo()
d.combo()
