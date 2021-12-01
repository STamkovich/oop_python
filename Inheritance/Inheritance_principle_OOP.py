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

# задачки
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

# Создайте класс NewInt, который унаследован от целого типа int,
# то есть мы будем унаследовать поведение целых чисел и значит экземплярам нашего класса будут поддерживать
# те же операции, что и целые числа.
# Дополнительно в классе NewInt нужно создать:
# метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2),
# обозначающее сколько раз нужно продублировать данное число. Метод repeat должен возвращать новое число,
# продублированное n раз (см пример ниже);
# метод to_bin, который возвращает двоичное представление числа в виде числа (может пригодиться функция bin)

class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])
