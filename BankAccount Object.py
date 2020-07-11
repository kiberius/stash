class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

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
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if type(balance) == int:
            if balance >= 0:
                self._balance = balance
            else:
                raise ValueError("'Money' must be positive!")
        else:
            raise ValueError("'Money' must be int!")

    def deposit(self, increase):
        if increase >= 0:
            self.balance += increase
            print(self)
        else:
            raise ValueError("'Increase' must be positive!")

    def withdraw(self, withdraw):
        if withdraw >= 0:
            self.balance -= withdraw
            print(self)
        else:
            raise ValueError("'Withdraw' must be positive!")
    def __repr__(self):
        return f"BankAccount - ({self.owner} : {self.balance})"

    def __str__(self):
        return f"Bank Account of {self.owner} has balance of {self.balance}."
