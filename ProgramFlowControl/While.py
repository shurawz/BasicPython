import random
highest = 10
ans = random.randint(0,10)
print("{}".format(ans))

guess = int(input("Please guess a number between 0 and 10:"))

# Aafaile lekheko hai guyz

while ( 0 <= guess < 11):
    if guess == ans:
        print("You got it.")
        break
    else:
        print("Now, you have 2 more chances.")
        guess = int(input())
        if guess == ans:
            print("You got it.")
            break
        else:
            print("Now, you have 1 last chance.")
            guess = int(input())
            if guess == ans:
                print("You got it.")
                break
            else:
                print("Fuck MotherFucker")
                break

