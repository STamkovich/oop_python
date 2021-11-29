# 3.10 Магические методы __iter__ и __next__ конспект
# При помощи этих меодо наши экземпляры класса смогут
# итерироваться тоесть эти методы позволят экземпляром класса обходиться в цикле for
class Mark:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call next marks')
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter

class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    # первый метод сделать наш класс итерабильным

    def __getitem__(self, item):
        return self.name[item]

    # второй метод через iter

    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print('call next student')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m = Mark([1, 2, 4, 3, 2, 5])
igor = Student('igor', 'Nikolaev',m)
for i in igor:
    print(i)
