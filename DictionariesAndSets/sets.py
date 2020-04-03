# farm_animals = {"sheep", "hen", "pig"}
# print(farm_animals) #It prints the farm_animals unorderly since set isnot defined in order before.
#
# for animals in farm_animals:
#     print(animals)
#
# wild_animals = set(["lion", "tiger", "panther", "leopard"])
# print(wild_animals)
#
# for animals in wild_animals:
#     print(animals)
#
# wild_animals.add("horse")
# farm_animals.add("horse")
#
# print(wild_animals)
# print(farm_animals)

#FOR THE BASIC OPERATION ON SET


even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuples = (4, 6, 9 ,16, 25)
square = set(square_tuples)
print(square)
print(len(square))

print(even.union(square)) #print(square.union(even)) also gives same result.
print(len(even.union(square)))

print(even.intersection(square)) #print(square.intersection(even)) also gives same result.
print(even & square)

print(even.difference(square))
print(even - square)
print(len(even.difference(square)))

print(square.difference(even))
print(square - even)
print(len(square.difference(even)))
