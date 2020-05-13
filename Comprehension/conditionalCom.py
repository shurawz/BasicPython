# CONDITIONAL COMPREHENSION

menu = [
    ["bacon", "spam", "yyat"],
    ["kukur", "biralo"],
    ["mobile", "charger", "bhaat"],
    ["bhaat", "maasu"]
]

meals = [meal for meal in menu if "spam" not in meal and "bhaat" not in meal]
print("First meals: {}".format(meals))

answer = [meal for meal in menu if ("spam" in meal or "bhaat" in meal) and not ("mobile" in meal and "charger" in meal)]
print("Second answer: {}".format(answer))
# In line 10, 1st meal is expression, 'for meal in menu' is iteration and 'if "spam" not in meal' is filer(s)
# In line 10 and 13, it is not allowed to add 'else' after the 'if'

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
