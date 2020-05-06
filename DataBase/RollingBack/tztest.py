import sqlite3
import pytz
import datetime
import pickle

# "https://www.sqlite.org/databyte3.html" if we want to study more on this topic click the link right behind this
# sentence

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, "
           "account TEXT NOT NULL, amount INTEGER NOT NULL, "
           "zone INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime' ) AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}".format(name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES (?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time()  # <-- unpacking the returned tuple
        pickle_zone = pickle.dumps(zone)

        db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES (?, ?, ?, ?)", (deposit_time, self.name, amount, pickle_zone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{:.2f} deposited.".format(amount))
        return self._balance

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance + (amount)
            # withdrawl_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (withdrawl_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print("{:.2f} withdrawn.".format(amount / 100))
            return amount / 100
        else:
            print("Amount must be greater than 0 and no more than your account balance.")
            return 0.0

    def show_balance(self):
        print("{}, your account has {:.2f} balance.".format(self.name, self._balance / 100))


# if __name__ == '__main__':
#     john = Account("John")
#     john.deposit(1010)
#     john.deposit(10)
#     john.deposit(10)
#     john.withdraw(30)
#     john.withdraw(0)
#     john.show_balance()
#
#     terry = Account("TerryJ")
#     graham = Account("Graham", 9000)
#     eric = Account("Eric", 7000)
#     michael = Account("Michael")
#     terryG = Account("TerryG")
#     db.close()
