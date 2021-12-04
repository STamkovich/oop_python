# Инструкция raise и пользовательские исключения
# при помощь инструкции raise можно возбуждать исключения в любой строчке вашего кода
# и при этом указывать сам тип исключения
try:
    {}['k']
    1 / 0
except (KeyError, IndexError) as error:
    print("LookupError")
    print(f'Logging erroe: {error} {repr(error)}')
    raise error from None
except ZeroDivisionError as err:  # присвоение псевдонима
    print("ZeroDivisionError")
    print(f'Logging erroe: {err} {repr(err)}')


# Пользовательские исключения
# все исключение лучше наследовать от Exception
# классы исключений можно переопределять
class MyException(Exception):  # создан класс исключений
    """this is my first Exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("str called")
        if self.message:
            return f'MyException ({self.message})'
        else:
            return "MyException is empty"


try:
    raise MyException('hello', 1, 2)  # рейзим
except Exception:
    print('done')
