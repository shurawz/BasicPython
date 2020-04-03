locations = {0: "You're sitting infront of your computer.",
             1: "You're standing at the end of a road before a small brick building.",
             2: "You're at top the hill.",
             3: "You're inside a building, a well house for a small stream",
             4: "You're in a valley beside a stream.",
             5: "You're in the forest."}

exits = [{"Q": 0},
          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          {"N": 5, "Q": 0},
          {"W": 1, "Q": 0},
          {"N": 1, "W": 2, "Q": 0},
          {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are: "+availableExits).upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction.")


