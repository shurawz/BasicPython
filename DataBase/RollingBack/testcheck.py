import sqlite3
import pytz
import pickle

db = sqlite3.connect('accounting.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    # print(row)
    utc_time = row[0]
    picked_zone = row[3]
    zone = pickle.loads(picked_zone)
    local_time = pytz.utc.localize(utc_time).astimezone(zone)

    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()

# SQLITE's date and time function is documented in the below site:-
# https://www.sqlite.org/lang-datefunc.html
