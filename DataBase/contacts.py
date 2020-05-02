import sqlite3

db = sqlite3.connect("contact.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contact (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contact (name, phone, email) VALUES ('Suraj', 2375, 'surajkoid@mail.com')")
db.execute("INSERT INTO contact VALUES ('Gotame', 283756, 'idofgotame@id.com')")

cursor = db.cursor()   # Cursor is called a Generator
cursor.execute("SELECT * FROM contact")

print(cursor.fetchall())  # It prints all the data items in a row
print(cursor.fetchone())  # It prints only one data item.
# IF particular number of fetchone() are executed then same number of data items are printed that are availabe otherwise
# prints None.

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()
