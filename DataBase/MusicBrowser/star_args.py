# single star unpacks tuple or lists where as double star unpacks dictionary.


def average(*args):  # if we dont write '*' before args then there will be error.
    mean = 0
    print("agrs: {}".format(args))  # without having'*' before args prints "args: (1, 2, 3, 4)".
    print("*args is ", *args)  # '*' before args unpacks the args tuple and prints "*args is  1 2 3 4".
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))


def build_tuples(*args):
    for arg in args[::-1]:
        print(arg[::-1], end=' ')  # prints "seson ecaf dnah daeh"


def smallest(*args):
    return max(args)


message_tuple = build_tuples("head", "hand", "face", "noses")
print(end='\n')
print(type(message_tuple))
print(message_tuple)

number_tuple = smallest(1, 2, 3, 4, 5)
print(type(number_tuple))
print(number_tuple)


# def print_backwards(*args, end=' ',**kwargs):
#     print(kwargs)
    # kwargs.pop('end', '\n')
    # for word in args[::-1]:
    #     print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, end=' ',**kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[::-1]:  # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)  # and prints the first word separately
    # print(end_character)  # which means we don't need this line

def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print_backwards(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backward.txt", 'w') as fuck:
    print_backwards("Haatti", "ghodaa", "kamilaa", "maachho", end='\n')
    print("Another String")

print()
print("hello", "friends", "this", "is", "bikash", "pandey", end='', sep='\n**\n')
print_backwards("hello", "friends", "this", "is", "bikash", "pandey", end='', sep='\n**\n')
print("=" * 15)