for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)


for multiple in [[(i, i * j) for j in range(1, 11)] for i in range(1, 11)]:
    print(multiple)

for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)