# num = int(input("Please enter any number: "))

# Aafaile gareko ho hai guyz
# rem = 0
# digit = 0
# count = 0
# rev = 0
# temp = 0
# while(num > 0):
#     rem = num % 2
#     digit = 10 * digit + rem
#     num = num // 2
#     count = count + 1
#
#
# for i in range(0,count):
#     temp = digit % 10
#     rev = rev * 10 + temp
#     digit = digit // 10
# print(rev)

powers = []
for i in range(15,-1,-1):
    powers.append(2 ** i)
print(powers)

