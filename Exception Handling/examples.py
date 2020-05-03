def factorial(n):
    if n <= 1:
        return 1
    else:
        print(100 / 0)
        return n * factorial(n-1)


try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print("It is very hard for us to process, please try smaller number.")
