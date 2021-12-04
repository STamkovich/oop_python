# Исключения в Python
# Исключения бывают: выполнения, до выполнения
# возможна обработка исключений
# так же имееться иерархия классов

# Обработка исключений try-except

try:  # оператор
    1 / 0
    int('hello')
    print('123')
    a + b
except ValueError:
    print('error ValueError')
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError")

# ещё ситуация
s = 'hello'
d = {}
try:  # оператор
    d['key']
    s[6]
except KeyError:
    print("error KeyError")
except IndexError:
    print("error IndexError")
#  но проще писать
try:
    4 + "fd"
except Exception:
    print('error')
finally:
    print('end')

# ситуация когда нужна инструкция finally
# этот блок будет выполнять всегда в независимости было ли тут исклечине
# finally может использоваться только один раз
f = open('123.txt')
try:
    execute(f)
finally:
    print('end')
    f.close()
# использование else
try:
    1/5
except(KeyError, IndexError):
    print("LookupError")
else:                    # else сработает тогда когда try не отловит исключения
    print('good')
finally:
    print('end')
# и ещё одна ситуация
print("hello")
print("hello1")
try:
    {}[5]
except LookupError:
    raise ValueError('Неправильное значение')
print("hello2")
print("hello3")
print("hello4")
print("hello5")

# типы исключений - являютсья классами
t = IndexError
isinstance(t, object)

# Исключения в функции
def thirs():
    print(("start third"))
    1 / 0
    print("finish third")


def second():
    print("start second")
    thirs()
    print("finish second")


def first():
    print("start first")
    try:
        second()
    except ZeroDivisionError:
        print("handling first")
    print('finish first')


print("hello")
first()


# Все исключения в Python
def printExcTree(thisclass, nest=0):
    if nest > 1:
        print(" |" * (nest - 1), end="")

    if nest > 0:
        print(" +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)


printExcTree(BaseException)


# задачка
# Реализуйте класс Wallet,аналог денежного кошелька, содержащий информацию о валюте и остатке имеющихся средств на счете
# В данном классе должны быть реализованы:
# метод __init__, который создает атрибуты currency и balance.
# Значения атрибутов currency и balance поступают при вызове метода __init__.
# При этом значение атрибута currency должно быть строкой, состоящей только из трех заглавных букв.
# Для этого необходимо сделать именно в такой последовательности следующие проверки
# В случае, если передается не строка, нужно возбуждать исключение TypeError с текстом "Неверный тип валюты" ;
# В случае, если передается строка, длина которой не равна трем символам,
# нужно возбуждать исключение NameError с текстом "Неверная длина названия валюты"
# В случае, если строка из трех символов состоит из незаглавных букв,
# нужно возбуждать исключение ValueError с текстом "Название должно состоять только из заглавных букв"
# метод __eq__, для возможности сравнивания балансов кошельков.
# Операция сравнения доступна только для кошельков с одинаковой валютой.
# Если валюты различаются, необходимо возбудить исключение ValueError с текстом "Нельзя сравнить разные валюты".
# При попытке сравнить экземпляр класса Wallet с другими объектами необходимо возбудить исключение
# TypeError с текстом "Wallet не поддерживает сравнение с <объектом>";
# методы  __add__ и __sub__ для возможности суммирования и вычитания кошельков.
# Складывать и вычитать мы можем только с другим экземпляром класса Wallet и только в случае,
# когда у них совпадает валюта (атрибуты currency).
# Результатом такого сложения должен быть новый экземпляр класса Wallet,
# у которого валюта совпадает с валютой операндов и значение баланса равно сумме/вычитанию их балансов.
# Если попытаются сложить с объектом не являющимся экземпляром Wallet или значения валют у объектов не совпадают,
# необходимо возбудить исключение ValueError с текстом  "Данная операция запрещена"
class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif currency != str(currency).upper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Wallet):
            if self.currency != other.currency:
                raise ValueError("Нельзя сравнить разные валюты")
            else:
                return self.balance == other.balance
        else:
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")

    def __add__(self, other):
        if isinstance(other, Wallet):
            if self.currency != other.currency:
                raise ValueError("Данная операция запрещена")
            else:
                return Wallet(other.currency, self.balance + other.balance)
        else:
            raise ValueError("Данная операция запрещена")

    def __sub__(self, other):
        if isinstance(other, Wallet):
            if self.currency != other.currency:
                raise ValueError("Данная операция запрещена")
            else:
                return Wallet(other.currency, self.balance - other.balance)
        else:
            raise ValueError("Данная операция запрещена")
