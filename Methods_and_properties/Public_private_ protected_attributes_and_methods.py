# 2.5 Публичные, приватные, защищенные атрибуты и методы

class BankAccount:
    def __init__(self, name, balance, pasport):
        self.__name = name
        self.__balance = balance
        self.__pasport = pasport

    def print_public_data(self):                           # публичный метод
        self.__print_private_data()

    def print_protected_data(self):                           # защищённый метод только между разработчиками
        print(self._name, self._balance, self._pasport)

    def __print_private_data(self):                           # приватный метод только между разработчиками
        print(self.__name, self.__balance, self.__pasport)

account = BankAccount('Bob', 10000, 433223432)
account.print_public_data()
#print(account._name)
#print(account._balance)
#print(account._pasport)

# что бы создать защищённый атрибут мы должны перед именем поставить одно нижнее подчёркивание
# что бы создать приватный атрибут мы жлджны перед именем поставить два нижних подчёркивания
# припомощт метода print_private_data происходит сокрытие обработки защищённых атрибутов
# или же этот метод называется инкапсуляция
# метод тоже может быть приватный и он тоже должен начинаться с двух подчёркиваний

# Итог: Инкапсуляция - механизм языка, позволяющий объединить данные и методы, работающие с этими данными,
# в единый объект и скрыть детали реализации от пользователя
