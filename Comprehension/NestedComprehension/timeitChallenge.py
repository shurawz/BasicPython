# CHALLENGE #
# SOLUTION 1
#
import timeit
from statistics import mean, stdev
#
# fact_test = """\
# def fact(n):
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result
#
# x = fact(130)
# """
# factorial_test = """\
# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# y = factorial(130)
# """
#
# result1 = timeit.timeit(fact_test, number=10000)
# result2 = timeit.timeit(factorial_test, number=10000)
# print("Face: {}".format(result1))
# print("Factorial: {}".format(result2))


# SOLUTION 2

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':

    # print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
    # print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=10000))

    # default value of repeat is 3
    list1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=6)
    list2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=6)

    print(sum(list1))
    print(sum(list2))

    # I I want to know on statistics:
    print(mean(list1), stdev(list1))
    print(mean(list2), stdev(list2))


# DOCUMENTATION FOR TIMEIT MODULE:

# https://docs.python.org/3/library/timeit.html

# DOCUMENTATION FOR STATISTICS MODULE:

# https://docs.python.org/3/library/statistics.html
