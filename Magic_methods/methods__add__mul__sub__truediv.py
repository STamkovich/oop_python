# 3.3 Магические методы __add__, __mul__, __sub__ и __truediv__
# __add__(+), __mul__(*),__sub__(-), __truediv__(/)

class BancAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BancAccount):  # проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance + other.balance  # слож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):  # проверяем явл ли числом
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, BancAccount):  # проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance * other.balance  # умнож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):  # проверяем явл ли строкой
            return self.name + other
        # raise NotImplemented

    def __rmul__(self, other):
        print('__rmul__ call')
        return self * other


r = BancAccount('Ivan', 900)  # __add__ call
print(r + 600, r.balance + 300, r.balance)  # 1500 1200 900
b = BancAccount('Luka', 1900)  # __add__ call
print(r + b, b + 600, b.balance + 300, b.balance)  # 2800 2500 2200 1900
print(600 + r)  # 1500


# __add__(+), __mul__(*),__sub__(-), __truediv__(/)

class BancAccount:
    def __init__(self, name, balance):
        print('New object __init__')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BancAccount):  # проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance + other.balance  # слож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):  # проверяем явл ли числом
            # return self.balance + other
            return BancAccount(self.name, self.balance + other)  # Возвращаем новый экземпляр
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other


t = BancAccount('Vasja', 900)  # New object __init__
print(id(t))  # 140062794291240
print(t + 30)  # Клиент Vasja с балансом 930

# задачка
# Вспомним нашего приятеля с предыдущих уроков: класс Vector.
#
# Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
#
# конструктор __init__, принимающий произвольное количество аргументов.
# Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка.
# Причем значения должны хранится в порядке неубывания;
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
# "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой.
# При этом значения должны быть упорядочены по возрастанию;
# "Пустой вектор", если наш вектор не хранит в себе значения
# переопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться
# с целым числом, в результате должен получиться новый Vector,
# у которого каждый элемент атрибута values увеличен на число
# с другим вектором такой же длины. В результате должен получиться новый Vector,
# состоящий из суммы элементов, расположенных на одинаковых местах. Если длины векторов различаются,
# выведите сообщение "Сложение векторов разной длины недопустимо";
# В случае, если вектор складывается с другим типом(не числом и не вектором), нужны вывести сообщение
# "Вектор нельзя сложить с <значением>"
# переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
# на целое число. В результате должен получиться новый Vector,
# у которого каждый элемент атрибута values умножен на переданное число;
# на другой вектор такой же длины. В результате должен получиться новый Vector, состоящий из произведения элементов,
# расположенных на одинаковых местах. Если длины векторов различаются,
# выведите сообщение "Умножение векторов разной длины недопустимо";
# В случае, если вектор умножается с другим типом(не числом и не вектором),
# нужны вывести сообщение "Вектор нельзя умножать с <значением>";
class Vector:

    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(self.values)}'
        else:
            return f'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[i + other for i in self.values])
        elif isinstance(other, Vector) and (len(other.values) == len(self.values)):
            return Vector(*[other.values[i] + self.values[i] for i in range(len(self.values))])
        elif isinstance(other, Vector) and (other.values != self.values):
            print(f'Сложение векторов разной длины недопустимо')
            return Vector()
        else:
            print(f'Вектор нельзя сложить с {other}')
            return Vector()

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[i * other for i in self.values])
        elif isinstance(other, Vector) and (len(other.values) == len(self.values)):
            return Vector(*[other.values[i] * self.values[i] for i in range(len(self.values))])
        elif isinstance(other, Vector) and (other.values != self.values):
            print(f'Умножение векторов разной длины недопустимо')
            return Vector()
        else:
            print(f'Вектор нельзя умножать с {other}')
            return Vector()
