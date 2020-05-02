import sqlite3

conn = sqlite3.connect('contact.sqlite')

for name, phone, email in conn.execute("SELECT * FROM contact"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

conn.close()