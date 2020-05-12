numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]  # Using Comprehension which is list comprehension
cubes = {number ** 3 for number in numbers}  # Using Comprehension which is set comprehension

# 'number ** 2' is a expression
# 'for number in numbers' is a iteration

print(squares)
print(sorted(cubes))
