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
