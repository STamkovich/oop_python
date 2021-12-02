# 4.4 Расширение класса в Python
# применяеться к дочерным классам

class Person:
    age = 25
    def breathe(self):
        print('Человек дышит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
            self.sleep()
        if hasattr(self, 'age'):
            print(self.age)


class Doctor(Person):
    age = 30

    def sleep(self):
        print('Доктор спит')

    def breathe(self):
        print('Доктор дышит')

    def walk(self):
        print('Доктор ходит')

p = Person()
p.combo()
d = Doctor()
d.combo()
