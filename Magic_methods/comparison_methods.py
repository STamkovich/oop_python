# 3.4 Специальные методы сравнения объектов классов

# __eq__ ==
# __ne__ !=
# __lt__ <
# __le__ <=
# __gt__ >
# __ge__ >=


class Restangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def area(self):
        return  self.a * self.b

    def __eq__(self, other):
        print('__eq__')
        if isinstance(other, Restangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__')
        if isinstance(other, Restangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        print('__le__')
        return self == other or self < other


f = Restangle(3, 4)
b  = Restangle(3, 4)

# задачка
# Для выражения относительной силы шахматистов используется система рейтингов. Наиболее популярная система рейтингов,
# которая используется Международной шахматной федерацией (ФИДЕ),
# большинством других шахматных федераций и игровых шахматных сайтов, является система рейтингов Эло.
# В зависимости от выступлений на различных соревнованиях каждому шахматисты начисляются баллы в его рейтинг.
# Давайте с вами реализуем класс ChessPlayer и научимся сравнивать рейтинги шахматистов между собой.
# И так, ваша задача реализовать класс ChessPlayer, который состоит из:
# метода инициализации, принимающего аргументы name, surname, rating;
# магического  метода __eq__,
# который будет позволять сравнивать экземпляры класса ChessPlayer с числами и другими экземплярами этого класса.
# Если сравнение происходит с целым числом и атрибут rating с ним совпадает, то необходимо вернуть True,
# в противном случае - False. Если же сравнение идет с другим шахматистом(экземпляром класса ChessPlayer)
# и значения атрибутов rating равны, то возвращается True, в противном случае - False.
# А если же сравнивается с другим типом данных, верните ‘Невозможно выполнить сравнение’;
# магического  метода __gt__.
# Если сравнение происходит с целым числом и атрибут rating больше его, необходимо вернуть значение True,
# в противном же случае - False. Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и
# атрибут rating у нашего экземпляра больше, то верните True, в противном случае - False.
# В случае если сравнение идет с остальными типами данных, верните ‘Невозможно выполнить сравнение’
# магического  метода __lt__.
# Если сравнение происходит с целым числом и атрибут rating меньше его,
# необходимо вернуть значение True, в противном же случае - False.
# Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и атрибут rating
# у нашего экземпляра меньше, то верните True, в противном случае - False.
# В случае если сравнение идет с остальными типами данных, верните ‘Невозможно выполнить сравнение’.

class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return f'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return f'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return f'Невозможно выполнить сравнение'
