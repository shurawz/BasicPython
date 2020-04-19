def fact(n):
    """ Calculate n! Factorial"""
    result = 1
    if n > 1:
        for x in range(2, n + 1):
            result *= x
    return result


def factorial(n):
    """ Calculate n! Factorial"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        f_zero = 0
        f_one = 1
        for n in range(1, n):
            result = f_zero + f_one
            f_zero = f_one
            f_one = result
    return result


for i in range(13):
    print(i, fibonacci(i))