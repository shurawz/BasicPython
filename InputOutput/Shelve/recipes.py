import shelve

#To upload recipes on the database using shelve.

# egg = ["egg", "onion", "oil"]
# rice = ["wheat", "water"]
pasta = ["pasta", "tomato"]

# recipes = shelve.open("recipe")

# recipes["egg"] = egg
# recipes["rice"] = rice
# recipes["pasta"] = pasta

# for item in recipes:
#     print(item, recipes[item])
# print(recipes)

# recipes.close()

#To update item list that was already uploaded. ((((( APPROACH 1 )))))

# recipes = shelve.open("recipe")


# temp_list = recipes["egg"]
# temp_list.append("love")
# recipes["egg"] = temp_list
#
# temp_list = recipes["pasta"]
# temp_list.append("oil")
# recipes["pasta"] = temp_list

# recipes["egg"] = recipes["egg"].append("love")
#
# for item in recipes:
#     print(item, recipes[item])
# print(recipes)


# recipes.close()

#To update item list that was already uploaded. ((((( APPROACH 2 )))))
recipes = shelve.open("recipe", writeback=True)

# The argument ' writeback ' makes the appended file be uploaded on cache rather than updating the db file as it
# ..it was done in the previous approach

recipes["pasta"] = pasta
recipes.sync()            # sync() function clears all the datas that are stored in the cache
pasta.append("oil")


for item in recipes:
    print(item, recipes[item])
# print(recipes)


# recipes.close