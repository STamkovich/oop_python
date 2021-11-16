# 2.6 Геттеры и сеттеры, property атрибуты

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balace = property(fget=get_balance, fset=set_balance, fdel=delete_balance) # свойства класса

# задачка
# Создайте класс UserMail, у которого есть:
# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
# Их необходимо сохранить в экземпляр как атрибуты login и __email (обратите внимание, защищенный атрибут)
# метод геттер get_email, которое возвращает защищенный атрибут __email ;
# метод сеттер set_email, которое принимает в виде строки новую почту. Метод должен проверять,
# что в новой почте есть только один символ @ и после нее есть точка. Если данные условия выполняются,
# новая почта сохраняется в атрибут __email, в противном случае выведите сообщение "Ошибочная почта";
# создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_address):
        if new_address.count('@') == 1 \
                and isinstance(new_address, str) \
                and new_address.count('.') == 1 \
                and '@.' not in new_address:
            self.__email = new_address
        else:
            print('Ошибочная почта')

    email = property(fget=get_email, fset=set_email)

