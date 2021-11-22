# практика по методам и свойствам
from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = "abra"

    @property
    def secret(self):
        s = input('Введите Ваш пороль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_numder(password):
        for i in digits:
            if i in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print("setter called")
        if not isinstance(value, str):
            raise TypeError('Пороль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Длинна пороля слишком мала, минимум должно быть 4 символа')
        if len(value) > 12:
            raise ValueError('Длинна пороля слишком велика, максимум должно быть 12 символов')
        if not User.is_include_numder(value):
            raise ValueError('Пороль должен содержать хотябы ожну цифру')
        self.__password = value


