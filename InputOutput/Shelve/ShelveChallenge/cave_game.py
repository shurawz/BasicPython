import shelve

locations = shelve.open("locations")

vocabulary = shelve.open("vocabulary")

loc = '1'
while True:
    availableExists = ", ".join(locations[loc]["exists"].keys())

    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        allExists = locations[loc]["exists"].copy()
        allExists.update(locations[loc]["namedExists"])

    direction = input("Available exists are: " + availableExists).upper()
    print()

    #Parse the user input, using our vocabulary dictonary if necessary\
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExists:
        loc = allExists[direction]
    else:
        print("You cannot go in that direction.")


locations.close()

vocabulary.close()

