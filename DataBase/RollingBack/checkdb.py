import sqlite3

db = sqlite3.connect('accounting.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

# Select query uses  SQLITE's strftime function to convert time field into a string
# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime' ) AS localtime,"
#                       "history.account, history.amount FROM history ORDER BY history.time"):

for row in db.execute("SELECT * FROM localhistory"):
    print(row)
    # utc_time = row[0]
    # local_time = pytz.utc.localize(utc_time).astimezone()
    # print("{}\t{}.".format(utc_time, local_time))

db.close()

# SQLITE's date and time function is documented in the below site:-
# https://www.sqlite.org/lang-datefunc.html
