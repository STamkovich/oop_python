# 2.10 Пространство имен класса
# мктоды находят имена только в глобальной области видимисти
#  в методах можно обращаться к именам класса черес self


class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.GO_DEV, self.PYTHON_DEV, self.REACT_DEV) # первый вариант через self

    def info2(self):
        print(DepartmentIT.REACT_DEV, DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV) # втарой вариант через сам ласс

    @property
    def info_prop(self):
        print(self.GO_DEV, self.PYTHON_DEV, self.REACT_DEV)  # третий через декоратор property(свойства)

    @classmethod
    def class_info(cls):
        print(cls.GO_DEV, cls.PYTHON_DEV, cls.REACT_DEV) # через дкоратор classmethod

    @staticmethod
    def static_info():
        print(DepartmentIT.GO_DEV, DepartmentIT.PYTHON_DEV, DepartmentIT.REACT_DEV) # через декоратор staticmathod

    def make_backend(self):
        print('Python and GO')

    def make_frontend(self):
        print('React')




it1 = DepartmentIT()