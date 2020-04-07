import shelve

# Important Note: When the with block is finishes, the program file is closed.
# By which we cannot access the file now onwards.

with shelve.open("frui") as fruit:
    # fruit['Orange'] = "fruit of mixture of red and yellow color"
    # fruit['Mango'] = "fruit of yellow color"
    # fruit['Apple'] = "fruit of red color"
    # fruit['Kiwi'] = "fruit of light green color"

    # print(fruit["Orange"])
    # print(fruit["Apple"])
    #
    # for item in fruit:
    #     print(item)

    for v in fruit.values():
        print(v)

    print(fruit.values())  #It shows ValuesView i.e .db file object

    for i in fruit.items():
        print(i)

    print(fruit.items()) #It shows itemValues i.e. .db file object

    # while True:
    #     shop = input("Write what you want from us: ")
    #
    #     if shop == "quit":
    #         break
    #
    #     if shop in fruit:
    #         description = fruit[shop]
    #         print(description)
    #     else:
    #         print("We dont have "+shop)

