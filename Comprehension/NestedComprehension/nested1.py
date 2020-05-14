burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

meal = [(burger, topping) for burger in burgers for topping in toppings]
print(meal)

# prints

# [('beef', 'cheese'), ('beef', 'egg'), ('beef', 'beans'), ('beef', 'spam'), ('chicken', 'cheese'), ....... ]

for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

# prints not in list.

# ('beef', 'cheese')
# ('beef', 'egg')
# ('beef', 'beans')
# ('beef', 'spam')
# ('chicken', 'cheese')
# ....

for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)

# prints

# [('beef', 'cheese'), ('chicken', 'cheese'), ('spicy bean', 'cheese')]
# [('beef', 'egg'), ('chicken', 'egg'), ('spicy bean', 'egg')]
# [('beef', 'beans'), ('chicken', 'beans'), ('spicy bean', 'beans')]
# [('beef', 'spam'), ('chicken', 'spam'), ('spicy bean', 'spam')]

for meal in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(meal)

# prints

# [('beef', 'cheese'), ('beef', 'egg'), ('beef', 'beans'), ('beef', 'spam')]
# [('chicken', 'cheese'), ('chicken', 'egg'), ('chicken', 'beans'), ('chicken', 'spam')]
# [('spicy bean', 'cheese'), ('spicy bean', 'egg'), ('spicy bean', 'beans'), ('spicy bean', 'spam')]

