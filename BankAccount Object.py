class BankAccount:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if type(owner) == str:
            self._owner = owner
        else:
            raise ValueError("'Owner' must be a str!")

    @property
    def money(self):
        return self._balance

    @balance.setter
    def money(self, money):
        if type(money) == int:
            if money >= 0:
                self._money = money
            else:
                raise ValueError("'Money' must be positive!")
        else:
            raise ValueError("'Money' must be int!")

    def deposit(self, increase):
        self.money += increase
        print(self)

    def withdraw(self, withdraw):
        self.money -= withdraw
        print(self)

    def __repr__(self):
        return f"BankAccount - ({self.owner} : {self.money})"

    def __str__(self):
        return f"Bank Account of {self.money} has balance of {self.money}."
