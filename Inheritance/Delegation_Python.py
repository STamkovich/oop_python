# 4.5 Делегирование в Python
# Делегирование это способ при котором в начальном классе вы можете вызвать метод родительского класса
# и вызывается он при помощи функции super()

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 50

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)

    def breathe(self):
        print('Человек вышит')


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname} - {self.age}'

    def breathe(self):
        print('Доктор дышит')
        super().breathe()  # функция super через неё мы обращаемся к родительскому методу


p = Person('Ivan', 'Ivanov')
d = Doctor('Ignat', 'Stirkin', 24)
print(p.name, p.surname)
print(d.name, d.surname, d.age)
d.info()
p.info()

# Задачки
# В этой задаче у нас будет один родительский класс Transport и три дочерних класса (Car, Boat, Plane).
# В классе Transport должны быть реализованы:
# метод __init__, который создает атрибуты brand, max_speed и kind. Значения атрибутов brand, max_speed,
# kind поступают при вызове метода __init__.
# При этом значение kind не является обязательным и по умолчанию имеет значение None;
# метод __str__, который будет возвращать строку формата:
# "Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".
# В классе Car должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue.
# Все значения этих атрибутов передаются при вызове класса Car.
# Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport,
# при этом атрибуту kind передайте значение "Car";
# свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина на <gasoline_residue> км";
# свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value,
# увеличивает уровень топлива gasoline_residue на переданное значение и затем вывести фразу
# 'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'.
# Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.
# В классе Boat должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, kind, owners_name.
# Все значения этих атрибутов передаются при вызове класса Boat.
# Внутри инициализации делегируйте создание атрибутов brand, max_speed, kind родительскому классу Transport,
# при этом атрибуту kind передайте значение "Boat";
# метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.
# В классе Plane должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand,
# max_speed, capacity. Внутри инициализации делегируйте создание атрибутов brand,
# max_speed, kind родительскому классу Transport, при этом атрибуту kind передайте значение "Plane";
# метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.
class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind="Car")
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки фвтомобиля')


class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind="Boat")
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind="Plane")
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'