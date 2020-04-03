# Creating Tuples

t = "Suraj", "is", "bad boy."
u = ("Blanket", "is", "on", "me.")
v = (("Ujyalo", "Din"))

songs = ("The Edge Band","Pokhara",2010,(1,"Mero Aashu"),(2,"Tashbir"),(3,"Nachhodnu Yo Saath"))

# printing tuples
# Difference between tuples and list is that tuples doesnot require parenthesis
# where as list requires sqaure paranthesis.
print(t)
print(u)
print(v)

# t[0] = "love" It is error b'coz in tuples value cannot be assigned.
# but it can be printed out that was assigned before.
print(songs)
# but can be reassignment on the previous tuples by changing values.

u = u[0], "isnot", u[2], "you."
print(u)

list = ["1234"]
print(list)

a, b, c, track1, track2, track3 = songs
print(t[0])

# But when a[0] is printed, it works as list which prints first character of first tuple

print(a)
print(b)
print(c)  # It prints 1st value, 2nd value and 3rd (Last) value of the tuple 'songs'
print(track1)
print(track2)
print(track3)


