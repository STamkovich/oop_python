# Магический метод __call__

# реализуем замыкание
from time import perf_counter


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'наш экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length


# изпользуем магичесткий метод __call__ в качестве декоратора

class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывается функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'функция отработала за {finish - start}')
        return result


# для тестирования создаём несколько функций
# функция нахождения факториала

@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= 1
    return pr


# функция нахождения чисел фибоначи

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)
