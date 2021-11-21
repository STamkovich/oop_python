# 2.9 Classmethod и staticmethod

# staticmethod - создаётся для того что бы можно было высзвать функцию и от класса и от экземпляра класса ток же
# он не привязываеться ни классу ни к экземпляру класса
#  так же staticmethod можно использовать когда нам нужна функция но мы её хотим реализовать именно внутри класса а не
#  выносить е вне класса
# такие методы нужны когда мы ходим делать обработку не над экземпляром класса а над самим классом


class Example:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instence_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')


    @classmethod
    def class_hello(cls):
        print(f'instence_hello {cls}')

# задачка
#  Создайте класс Robot, у которого есть:
# атрибут класса population. В этом атрибуте будет хранится общее количество роботов, изначально принимает значение 0;
# конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение
# вида "Робот <name> был создан".
# Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")
