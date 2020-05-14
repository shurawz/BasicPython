locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

loc = 1
# locate = [locations[ex] for ex in exits if loc in exits[ex].values()]
# print(locate)
#
# for loc in locations:
#     locate = [(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
#     print("Location loading to {}".format(loc), end="\t")
#     print(locate)

forest = []
for ex in exits:
    if loc in exits[ex].values():
        forest.append(locations[ex])
print(forest)
print()
# for loc in locations:
#     for ex in exits:
#         if loc in exits[ex].values():
#             print((ex, locations[ex]))
#     print("\n")

for loc in locations:
    forest = []
    for ex in exits:
        if loc in exits[ex].values():
            forest.append((ex, locations[ex]))
    print("Location leading to {}".format(loc), end="\t")
    print(forest)