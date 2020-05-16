# CHALLENGE
# SOLUTION 1

import timeit
#
# setup = """\
# text = "My name is Anthony Gunsalves."
# """
#
# letter = """\
# def letter():
#     map_capitals = list(map(str.upper, text))
#     return map_capitals
#
#     capitals = [char.upper() for char in text]
#     return capitals
# """
# word = """\
# def word():
#     map_capitals = list(map(str.upper, text.split(' ')))
#     return map_capitals
#
#     capitals = [word.upper() for word in text.split(' ')]
#     return capitals
# """
#
# print(timeit.timeit(letter, setup, number=10000))
# print(timeit.timeit(word, setup, number=10000))

# SOLUTION 2


text = "My name is Anthony Gunsalves."


def letter():
    capitals = [char.upper() for char in text]
    return capitals



def letter_map():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def word():
    capitals = [word.upper() for word in text.split(' ')]
    return capitals


def word_map():
    map_capitals = list(map(str.upper, text.split(' ')))
    return map_capitals


if __name__ == '__main__':
    print(timeit.timeit(letter, number=10000))
    print(timeit.timeit(letter_map, number=10000))
    print(timeit.timeit(word, number=10000))
    print(timeit.timeit(word_map, number=10000))

    print(letter()) 
    print(letter_map())
    print(word())
    print(word_map())
