# 2.1 Методы экземпляра. Аргумент self


class Cat:
    breed = 'pers'
    def hello(*args): # *args произвольное количество аргументов
        print("Hello world from kitty", args)

    def show_breed(self):
        print(f"my breed is {self.breed}")

    def show_name(self):
        if hasattr(self, 'name'):
            print(f"my name is {self.name}")
        else:
            print('nothing')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age


# метод это тажа функция но она объявлена внутри нашего класса
# метод отличаеться от функции тем что метод привязан к конкртному объекту тоесть он будет связан сним
# функция ни скем не связана и её можно отдельно вызывать
# функция вызываеться именно к какомто объекту и она с ним будет связана
# ВАЖНО!!! При вызове метода тот объект с которым он связан автоматически будет проставляться во аргумент функции
