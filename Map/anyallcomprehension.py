from data import people, plants_list, Plant, plants_dict
#

if all([person[1] for person in people]):
    print("Sending email")
else:
    print("User not defined.")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This container contains atleast a grass")
else:
    print("Better luck next time")


if any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("Atleast a grass found.")
else:
    print("Found Nothing")

if any([plant.plant_type == "Cactus" for plant in plants_dict.values()]):
    print("Atleast a cactus found.")
else:
    print("Found Nothing")

