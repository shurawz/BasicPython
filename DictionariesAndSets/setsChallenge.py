aWord = "gotamey"
print(aWord)

print(set(aWord))

vowels = frozenset('aeiou')

finalSet = set(aWord).difference(vowels)
print(finalSet)
print(len(finalSet))