import pytz
import datetime

class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list =[(Account._current_time(), balance)]
        print("{}, your account is created.".format(self._name, self._balance))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("You withdrawing amount must be less than your current balance. Thank You")
        self.show_balance()

    def show_balance(self):
        print("Dear {0}, your balance is {1}.".format(self._name, self._balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
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
