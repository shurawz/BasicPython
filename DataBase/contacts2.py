import sqlite3

db = sqlite3.connect("contact.sqlite")

# new_email = "otherupdate@uup.date"
# phone = input("Please enter your number.")
#
# update_sql = "UPDATE contact SET email = '{}' WHERE phone = {}".format(new_email, phone) #placeholders
# print(update_sql)
#
# update_cursor = db.cursor()
# update_cursor.executescript(update_sql)

# For the complex programs I guess, actually solution for how to use the placeholders
new_email = "newmail@up.date"
phone = input("Please enter your number.")

update_sql = "UPDATE contact SET email = ? WHERE phone = ?" #placeholders
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))



print("{} row updated.".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contact"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

# db.commit()
db.close()

# It is okay to call commit function either of the cursor and db
# But in complex programs we make many functions, for each function, particular commit funtion should be used
# To avoid bugs.
