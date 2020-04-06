import pickle
#Since pickle is the library which is to be called when it is going to be used.

# Pickling: It is a process where a Python object hierarchy is converted into a byte stream.
# Unpickling: It is the inverse of Pickling process where a byte stream is converted into an object hierarchy

# dumps() – This function is called to serialize an object hierarchy.
# loads() – This function is called to de-serialize a data stream.

gotamey = ("Suraj Gotamey",
           "Bachelors",
           2020,
           ((1, "Python"), (2, "Applied Opearting System"), (3, "System Programming")))

even = range(0,10,2)
odd = range(1,11,2)
number = 27365

with open("gotamey.pickle", 'wb') as pickle_file:

    #line 23 to 26 is to write

    pickle.dump(gotamey, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(number, pickle_file)

with open("gotamey.pickle", 'rb') as pic_f:

    #line 32 to 35 is to load them back in

    tuple = pickle.load(pic_f)
    even_list = pickle.load(pic_f)
    odd_list = pickle.load(pic_f)
    num = pickle.load(pic_f)

print(tuple)

name, level, year, subject = tuple
print("Name: ",name)
print("Level: ",level)
print("Year: ",year)

for sub in subject:
    subNum, subName = sub

    print(subNum, end= ' ')
    print(subName)

print("-" * 40)

for item in even_list:
    print(item)

print("-" * 40)

for item in odd_list:
    print(item)

print("-" * 40)

print(num)