# Методы __getitem__ , __setitem__ и __delitem__
# ппри помощи этих методов можно добавть обращение по индексу к нашим объектам

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    # что бы обращаться в консоле к значению в списке по индексу необходим метод __getitem__

    def __getitem__(self, item):  # значение item поздразумевает собой индекс
        if 1 <= item <= len(self.values):  # хитрасть что бы в носоле индексы начинались с 1
            return self.values[item - 1]
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    # что бы изменять значение по индексу в консоле понадобится мотод __setitem__
    # разряженного массива - это такая коллекция в которой некоторые значения просто пропущенные

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):  # создание разряженного массива
            self.values[key - 1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)  # метод extend помогает увеличить один список при помощи другого
            self.values[key - 1] = value
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    # что бы удалить индекс из нашей коллекции на понадобится метод __delitem__

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами нашей коллекции')


# dict
class Dictionary:

    def __init__(self, dct):
        if not isinstance(dct, dict):
            raise TypeError('Wrong type')
        self.dct = dct

    def __str__(self):
        return str(self.dct)

    def key_exists(self, key):
        if (not isinstance(key, (str, int, tuple)) or
                key not in self.dct):
            raise KeyError(f'Ключа {key} не существует')
        return True

    def __getitem__(self, item):
        if self.key_exists(item):
            return self.dct[item]

    def __setitem__(self, key, value):
        if self.key_exists(key):
            self.dct[key] = value

    def __delitem__(self, key):
        if self.key_exists(key):
            del self.dct[key]


inp = {1: 1, '2': '2', ('t', 'u'): 'tuple'}
d = Dictionary(inp)
d[1] = 'One'
del d['2']
print(d[1])  # One
print(d)  # {1: 'One', ('t', 'u'): 'tuple'}
