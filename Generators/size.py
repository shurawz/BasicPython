import sys


def in_range(n: int):
    start = 0
    while start < n:
        print("It is returning {}.".format(start))
        yield start
        start += 1


_ = input("line 11")
big_range = in_range(5)
_ = input("line 13")

# next function use jun code ko maathi garexa tyo vanda talako code 1 time execute vayesi matra 1st code execute hunxa
print(next(big_range))
print(next(big_range))
print(next(big_range))
print(next(big_range))
print(next(big_range))

print("Size of 'big_range' is {} bytes.".format(sys.getsizeof(big_range)))

big_list = []

_=  input("line 18")
for val in big_range:
    _ = input("line 20")
    big_list.append(val)


print("Size of 'big_list' is {} bytes.".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
