# 4.1 Принцип наследования в ООП
# Принцип наследования помогает избавиться от дублирования кода(одиноковаые атрибуты либо поведение)
# колличество уровней наследования практически неограничено
# класс родитель(базовый, parent)
class Person:

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):  # подкласс родительского класса (subclass)

    def can_cure(self):        # рассширает функциогальность класса Person (extend)
        print('Я могу лечить')

class Ortoped(Doctor):
    pass

class Architect(Person):  # подкласс родительского класса (subclass)

    def can_build(self):
        print('Я могу построить здание')


d = Doctor()
d.can_cure()
d.can_breathe()
a = Architect()
a.can_build()
a.can_breathe()
print(issubclass(Doctor, Person))  # функция которая проверяет являеться ли один класс подклассом второго
print(isinstance(d, Doctor))  # функция которая проверяет принадлежит ли экземпляр классу
print(isinstance(d, Person))


class Vehicle:
    pass

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass

class Race_Car(Car):
    pass