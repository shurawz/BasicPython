import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please enter again.")
        except EOFError:
            sys.exit(1)

# If 'while True:' na vaako vaye the on line 2, the output would be lines 10, 11, 12.

# Please enter first number: kjb
# Invalid number entered, please enter again.
# Please enter second number

# 'while True' line 2 maa xa so first_number le correct value na paaye samma second_number lina jaadaina.


first_number = getint("Please enter first number")
second_number = getint("Please enter second number")

try:
    print("{} is divided by {} to get {}.".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by 0.")
    sys.exit(2)

