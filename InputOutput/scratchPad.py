# print("Gotamey".strip('y')) #Strip() function removes the letter either from begining or from the end of the word.
#
# print("#"*40)
#
# print("Gotamey".strip('eyst')) #It removes only the characters which are available in the word in the same manner.

# city = "Ilam", "Lalitpur", "Okhaldhunga", ((1,"Pokhara"), (2,"Kusma"), (3,"Shigi"))

# with open("city.txt", 'w') as cit:
#     for ci in city:
#         print(ci, file=cit)
#
# # print(city)
# for ci in city:
#     print(ci)


# with open("city.txt",'w') as cit:
#     print(city, file=cit)

city=[]

with open("city.txt", 'r') as okl:
    content = okl.readline()

jo = eval(content)
print(jo)
num1, num2, num3, num4 = jo
print(num1)
print(num2)
print(num3)



