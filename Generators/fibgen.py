""" A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with
    the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a
    generator function."""


def fibonacci():

    current, previous = 0, 1
    while True:
        yield current  # yield in generator is like return in function
        current, previous = current + previous, current


fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))