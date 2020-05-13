numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number. I'll tell you its square value: "))

squares = [number ** 2 for number in numbers]  # Using Comprehension which is list comprehension
# cubes = {number ** 3 for number in numbers}  # Using Comprehension which is set comprehension

# 'number ** 2' is a expression
# 'for number in numbers' is a iteration

indx = numbers.index(number)
print(squares[indx])
# print(sorted(cubes))
