for i in range(1,12):
    print("The value of {0} when squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# #If program flow

name = input("Please enter your name: ")

#Remember, input paxi kunai pani haalat maa print function jaana mandaina hai guyz
age = int(input("How old are you, {0} ?".format(name)))


if age >= 14:
    print("Congratulations, You can watch porn.")
else:
   print("Sorry but please come back in {0} years.".format(14 - age))


#Use of elseif, but in python elseif is elif

print("Please guess a number.")
guess = int(input())

if guess > 5:
    print("You are given with one more chance.")
    guess = int(input())
    if guess == 5:
        print("You got it correct.")
    else:
        print("Again, you're wrong my friend.")
elif guess < 5:
    print("You are given with one more chance.")
    guess = int(input())
    if guess == 5:
        print("You got it correct.")
    else:
        print("Again, you're wrong my friend.")
else:
    print("You're right on your first attempt.")


# Aafaile gareko ho hai guyz1

print("Please guess a number between 0 and 10.")
guess = int(input())
if guess < 10 and guess > 0: # 0 ra 10 vanera mention garna jaruri xa
    while(guess != 5 ):
        print("You're a wrong.")
        print("You are provided with one more chance.")
        guess = int(input())
    print("You got right answer.")
else:
    print("The number is out of the range.")


# Advanced use of If, ElseIf, and Else

# Whenever is it is empty or '0' inside the braces then it is said to be false.

# Now,

x = input("Please enter something.")

if x:
    print("You enteredGi '{}'.".format(x))
else:
    print("You did not enter anything.")

print(not False) #Just G.K. hai guyz
print(not True)

parrot = "Seto Sugaa"
letter = input("Enter a character")

if letter in parrot:
    print("{} is available.".format(letter))
else:
    print("{} isnot available.".format(letter))