# cities = ["Pokhara", "Kathmandu", "Baglung", "Birgunj"]
#
# with open("cities.txt", 'w') as tet:
#     for line in cities:
#         print(line, file=tet)



cities =[]
# with open("cities.txt", 'r') as tet:
#
#     for city in cities:
#         print(city) #Since, the file 'cities' has nothing to display or print, it displays nothing
#

with open("cities.txt", 'r') as gif:
    for city in gif:
        cities.append(city)
print(cities)

for city in cities:
    print(city)
