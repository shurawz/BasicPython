import pytz
import datetime

class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list =[]
        print("{}, your account is created and your current balance is {}.".format(self.name, self.balance))
        # self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("You withdrawing amount must be less than your current balance. Thank You")
        self.show_balance()

    def show_balance(self):
        print("Dear {0}, your balance is {1}.".format(self.name, self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

account = Account("Suraj Gotamey", 0)
account.deposit(5000)
# account.withdraw(6000)
account.withdraw(3456)
account.show_transaction()
