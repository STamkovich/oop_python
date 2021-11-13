# 2.2 Инициализация объекта. Метод init

# магический метод(функция) init он начинаеться с двух подчёркиваний и заканчиваеться
# метод init срабатывает после создания объектов
# метод init нужен для инициализации то есть для заполнения нашего  объекта значениями
# аргументы в методе можно называть как хочешь

class Cat:


    def __init__(self, name, breed = 'pers', age=1, color='white'):
        print('Hello new object is', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

# задачки
#  Создайте класс Laptop, у которого есть:
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price
# и также атрибут laptop_name - строковое значение, вида "<brand> <model>"
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"
# И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.


class Laptop:


    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"

laptop1 = Laptop('Asus', '18-bdfx', 37000)
laptop2 = Laptop('Samsung', '13-bsdf0xx', 47000)

# Создайте класс SoccerPlayer, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: name, surname.
# Также во время инициализации необходимо создать 2 атрибута экземпляра:
# goals и assists - общее количество голов и передач игрока, изначально оба значения должны быть 0
# метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;
# метод make_assist, который принимает количество передач, сделанных игроком за матч,
# по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
# метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>

class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


#  Создайте класс Zebra, внутри которого есть метод which_stripe ,
#  который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"
# Пример работы с классом Zebra

class Zebra:

    def __init__(self):
        self.count = 1

    def which_stripe(self):
        if self.count % 2 == 1:
            self.count += self.count
            print("Полоска белая")
        else:
            self.count += 1
            print("Полоска черная")


# Создайте класс Person, у которого есть:
# конструктор __init__, принимающий 3 аргумента: first_name, last_name, age.
# метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;

class Person:
    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
