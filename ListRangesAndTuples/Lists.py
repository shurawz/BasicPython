# ipAdd = input("Enter the IP Address: ")
# print(ipAdd.count("."))

# parrot = ("tall", "small", "average")
#
# for state in parrot:
#     print("He is {}".format(state))
#
# even = [0, 2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# number = even + odd
# # number.sort()
# print(sorted(number))
#
# even = [2, 4, 6, 8]
#
# revEven = sorted(even,reverse = True)
# # Sorted function uses two parameters i.e. Lists and another function is kind of reverse.
#
# print(revEven is even) #if revEven is really same as even then it returns true otherwise it returns false.
# print(even)
# if revEven != even:
#     print(revEven)

meal = list()

meal.append(["egg", "spam", "bacon"])
meal.append(["egg", "sausage", "bacon"])
meal.append(["egg", "spam"])
meal.append(["egg", "bacon", "spam"])
meal.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
meal.append(["egg", "spam", "sausage", "spam"])

# print(meal)

for item in meal:
    if not "spam" in item:
        print(item)
        for incredients in item:
            print(incredients)