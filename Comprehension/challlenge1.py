text = input("Enter your text here: ")  # 'Suraj Gotamey'

answer = [x for x in text.split()]
print(answer)

output = [(x, len(x)) for x in text.split()]
print(output)

# If we make list comprehension to set comprehension then it won't print more than one word in the text.
# avoiding duplicates I would say
