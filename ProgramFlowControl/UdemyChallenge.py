# Udemy Challenge

# name = input("Enter your name")
# age = int(input("And your age? "))
#
# if age > 18 and age < 31:
#     print("Congratulations, you '{0}' can enjoy your holidays.  ".format(name))
# elif age > 30:
#     print("It is your time to do hard work for your future.")
# else:
#     print("You've to come back in {} years".format(18-age))
#
# # Now, For loop
#
# for i in range(1, 5):
#     for j in range(1, i):
#         print("*",end='') #end function means 'in the same line'
#     print("\n")
#
number = "9,233,345,768,34,456"
cleanNumber = ''
for char in number:
    if char in "0123456789":
        cleanNumber = cleanNumber + char
newNumber =cleanNumber
print("Cleaned number is: "+newNumber)

guess = ("1234" , "4321")
for state in guess:
    print("He said'{}'".format(state))




