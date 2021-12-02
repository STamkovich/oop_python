# 4.6 Множественное наследование
#  Множественное наследование - это такая ситуация когда ваш класс имеет несколько родителей

class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура я отучился на доктора')

    def can_build(self):
        print("Я человек, я тоже умею строить, но не очень")


class Builder:

    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ура я отучился на строителя')

    def can_build(self):
        print("Я строитель, я умею строить")


class Person(Doctor, Builder):

    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self):
        print('Посмотрим кем я стал')
        super().graduate()
        Doctor.graduate(self)  # таким способом мы вызвали метод graduate у класса Doctor


s = Person(24, 'spec')
s.can_build()
print(Person.__mro__)
