
with open("cities.txt", 'a') as tet:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tet)
        print("-" * 30, file=tet)



