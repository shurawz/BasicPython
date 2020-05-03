import sqlite3

conn = sqlite3.connect('contact.sqlite')

name1 = input("Please enter the name: ")
# cursor = conn.cursor()


for row in conn.execute("SELECT * FROM contact WHERE name LIKE ?", (name1,)):
    print(row)
    print("-" * 20)

# cursor.close()
conn.close()
