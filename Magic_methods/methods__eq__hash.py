# 3.5 Магические методы __eq__ и __hash__

# hash можно найти только у неизменяемых объектов

# Тема сильно недораскрыта: начнем с того, почему поломался хэш?
# Дело в том, что для разрешения коллизий (ситуаций, при которых несколько объектов имеют одинаковый хэш)
# используется метод __eq__, который позволяет исключить объекты, считающиеся одинаковыми.
# Поскольку по умолчанию def __eq__(self, other): return id(self)==id(other), то все объекты считаются уникальными,
# несмотря на то, что их хэш может совпадать (реализация хэш-функции зависит от интерпретатора и алгоритма хэширования,
# Добавление метода __eq__ приводит к неопределенности, связанной с уникальностью объектов,
# стандарт Python требует от разработчиков ее разрешения, заставляя переопределить в классе метод __hash__.
#
# Собственно, разрешение коллизий и определяет вставку ключей и значений в словари. Сначала немного кода:

class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(3, 4)
p2 = Point(3, 4)
tuple1 = (3, 4)
dict1 = {p1: 1, p2: 2, tuple1: 3}

print(hash(p1), hash(p1) == hash(p2) == hash(tuple1))  # число, True
print(dict1)  # {<__main__.Point object at 0x...>: 2, (3, 4): 3}

# Добавление ключей, значений в словарь идет в порядке очереди:
# {p1: 1}
# на следующем шаге возникает коллизия, поскольку p1==p2, то ключ не переписывается, значение обновляется:
# {p1: 2}
# на следующем шаге опять возникает коллизия, но p1 != tuple1,
# поэтому в словарь добавляется ещё один ключ со своим значением:
# {p1: 2, tuple1: 3}
# Похожая ситуация описана у Бейдера в "Чистом Python'е":
# dict2 = {True: 0, 1.0: 1, 1: 2}
# print(dict2)  # {True: 2}
# Из-за того, что хэш True, 1 и 1.0 совпадает и True == 1 == 1.0,
# то в итоговом словаре у нас будет только один ключ (указанный первым) и одно значение (указанное последним).