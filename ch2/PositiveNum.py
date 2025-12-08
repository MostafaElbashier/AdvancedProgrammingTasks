class Positive:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        instance.__dict__[self.name] = value
class BankAccount:
    balance = Positive("balance")
    def __init__(self, amount):
        self.balance = amount
acc = BankAccount(100)
print(acc.balance)  
