sentence = "What the hell is going on guyz ?"

capitals = [char.upper() for char in sentence]
print(capitals)

words = [word.upper() for word in sentence.split(' ')]
print(words)

print([word for word in sentence.split(' ')])

magic = sentence.split(' ')
print(magic)
