# If I want to know more about other builtin functions like 'enumerate', I can visit the link mentioned below:
# docs.python.org/3/library/functions.html
import timeit

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

nested_loop = """\
exit_to_destination1 = []
for loc in sorted(locations):
    exit_to_destination1 = []
    for ex in exits:
        if loc in exits[ex].values():
            exit_to_destination1.append((ex, locations[ex]))
    print("Locations leading to {}".format(loc), end="\t")
    print(exit_to_destination1)
"""
print()
print("List Comprehension")
print("------------------")
loop_comp = """\
for loc in sorted(locations):
    exit_to_destination2 = [(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
    print("Locations leading to {}".format(loc), end="\t")
    print(exit_to_destination2)
"""
print()
print("Nested Comprehension")
print("------------------")

nested_comp = """\
exit_to_destination3 = [[(ex, locations[ex]) for ex in exits if loc in exits[ex].values()] for loc in sorted(locations)]
# print("Locations leading to {}".format(loc), end="\t")
for index, loc in enumerate(exit_to_destination3):
    print("Location leading to {}".format(index), end="\t")
    print(loc)
"""

result1 = timeit.timeit(nested_loop, globals=globals(), number = 1000)
print("Nested Loop:\t{}".format(result1))
