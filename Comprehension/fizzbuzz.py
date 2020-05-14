for x in range(1, 31):
    fizzbuzz = "Fizz Buzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)

# Challenge

fizzbuzz = ["Fizz Buzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else str(x)
            for x in range(1, 31)]
print(fizzbuzz)

for fb in fizzbuzz:
    print(fb.center(12, '*'))
