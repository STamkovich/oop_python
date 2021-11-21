# 2.7 Декоратор Property

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance

a = BankAccount(**{'name': 'Illia', 'balance': 5})
z = a.my_balance
c = a.name


# задачка
#  Создайте класс Money, у которого есть:
# конструктор __init__, принимающий 2 аргумента: dollars, cents.
# По входным аргументам вам необходимо создать атрибут экземпляра total_cents.
# свойство геттер dollars, которое возвращает количество имеющихся долларов;
# свойство сеттер dollars, которое принимает целое неотрицательное число -
# количество долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents,
# при этом значение центов должно сохранятся. В случае, если в сеттер передано число,
# не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";
# свойство геттер cents, которое возвращает количество имеющихся центов;
# свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100
# - количество центов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents,
# при этом значение долларов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию,
# нужно печатать на экран сообщение "Error cents";
# метод __str__ (информация по данному методу),
# который возвращает строку вида "Ваше состояние составляет {dollars} долларов {cents} центов".
# Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами
# В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!
class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and int(value) >= 0:
            self.total_cents = int(value) * 100 + self.total_cents % 100
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and int(value) < 100:
            self.total_cents = self.total_cents - self.total_cents % 100 + int(value)
        else:
            print("Error cents")

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'