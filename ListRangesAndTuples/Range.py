# print(range(0,100)) #It prints range(0,100)
# print(list(range(0,100))) #It prints from 0 to 100 as a list
# print(list(range(0,100,2))) #It prints from0 to 100 ith the differece of 2. For example: 0, 2, 4, 6, .....

# item = range(0, 100, 2)
# print(item.index(4)) #It prints the value or address of the given number i.e. '4'
#
# bich = range(7,1000,7)
#
# guess = int(input("Please, guess a number less than 1000: "))
#
#
# if guess in bich:
#     print("Successful.")

decimals = range(0,100,3)
bich = decimals[0:100:3]

print(decimals[0:100:3] == bich[0:100:3])
