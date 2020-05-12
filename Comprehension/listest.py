"""
    Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set,
    dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of
    comprehensions:

    List Comprehensions
    Dictionary Comprehensions
    Set Comprehensions
    Generator Comprehensions
"""

print(__file__)  # prints whole path, also the file name:
# 'C:/Users/Suraj Gotamey/Desktop/BasicPython/Comprehension/listest.py'

numbers = [1, 2, 3, 4, 5, 6]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

