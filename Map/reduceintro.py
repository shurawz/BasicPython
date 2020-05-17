import timeit
import functools


def calc_values(x, y: int):
    return x * y


numbers = [2, 8, 5, 9, 13]

result1 = 1
for x in numbers:
    result1 *= x
print(result1)

reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
# print(sum(numbers))

result = calc_values(2, 8)
result = calc_values(result, 5)
result = calc_values(result, 9)
result = calc_values(result, 13)
print(result)
