from data import basic_plants_list, plants_list

for plant in plants_list:
    print(plant[0])

# for plant in plants_list:
#     print(plant)

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')
print(example)


