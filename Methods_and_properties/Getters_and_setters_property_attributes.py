# 2.6 Геттеры и сеттеры, property атрибуты

class BankAccount:  # создание класса

    def __init__(self, name, balance):  # инициализация объекта и переменных
        self.name = name  # присвоение атрибуту класса self.name значение переменной name
        self.__balance = balance  # то же самое

    def get_balance(self):  # метод получаения баланса
        return print('Мой баланс -', self.__balance)  # возврат сообщения о балансе

    def set_balance(self, value):  # метод пополнения баланса
        if not isinstance(value, (int, float)):  # проверям, передано число или дробно число
            raise ValueError('баланс должен быть числом')  # если нет, то выводим сообщение
        self.__balance = value  # если число подходит, то изменяем атрибут класса self.__balance на переданное значение в value
        print('Баланс пополнен на  - ', self.__balance)  # печатаем сообщение если баланс успешно пополнен

    def delete_balance(self):  # метод удаления баланса
        del self.__balance  # удаляем баланс
        print('Баланс удалён')  # уведомление после удаления баланса


balance = property(fget=get_balance,
                   # используем функцию Property() для того чтобы сократить запись и повысить удобство работы с классом
                   fset=set_balance,  # fget=get_balance устанавливает метод удаления баланса
                   fdel=delete_balance)  # fset=set_balance устанавливаем метод пополнения баланса
# fdel=delete_balance устанавливает метод удаления баланса

acc1 = BankAccount('Pasha', 1_000_000_000)  # создаём экземпляр класса, и передаём имя и баланс


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
