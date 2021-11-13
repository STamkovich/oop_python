# 2.1 Методы экземпляра. Аргумент self


class Cat:
    breed = 'pers'
    def hello(*args): # *args произвольное количество аргументов
        print("Hello world from kitty", args)

    def show_breed(self):
        print(f"my breed is {self.breed}")

    def show_name(self):
        if hasattr(self, 'name'):
            print(f"my name is {self.name}")
        else:
            print('nothing')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age
#
# метод это тажа функция но она объявлена внутри нашего класса
# метод отличаеться от функции тем что метод привязан к конкртному объекту тоесть он будет связан сним
# функция ни скем не связана и её можно отдельно вызывать
# функция вызываеться именно к какомто объекту и она с ним будет связана
# ВАЖНО!!! При вызове метода тот объект с которым он связан автоматически будет проставляться во аргумент функции

# задачки
# Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
# Пример работы с классом Lion
# simba = Lion()
# simba.roar() # печатает Rrrrrrr!


class Lion:


    def roar(self):
        print("Rrrrrrr!!!")

# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить метод start_from,
# который принимает один необязательный аргумент - значение, с которого начинается подсчет, по умолчанию равно 0
# Также нужно создать метод increment, который увеличивает счетчик на 1.
# Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset,
# который обнуляет экземпляр счетчик

class Counter:

    def start_from(self, value=0):
        self.value = value
    def increment(self):
        self.value += 1

    def display(self):
        print(f'"Текущее значение счетчика = {self.value}"')

    def reset(self):
        self.value = 0


# Создайте класс Point. У этого класса должны быть

# метод set_coordinates, который принимает координаты по x и по y,
# и сохраняет их в экземпляр класса соответственно в атрибуты x и y
# метод get_distance, который обязательно принимает экземпляр класса Point
# и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение "Передана не точка"
# Пример работы с классом Poin

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distanse(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print("Передана не точка")