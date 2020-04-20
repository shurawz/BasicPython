class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("{}, your account is created and your current balance is {}.".format(self.name, self.balance))
        # self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
        else:
            print("You withdrawing amount must be less than your current balance. Thank You")
        self.show_balance()

    def show_balance(self):
        print("Dear {0}, your balance is {1}.".format(self.name, self.balance))


account = Account("Suraj Gotamey", 0)
account.deposit(5000)
# account.withdraw(6000)
account.withdraw(3456)
