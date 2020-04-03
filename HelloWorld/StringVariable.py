parrot = 'Lemondwaski'
print("Parrot =" + parrot)

print(parrot[3])
print(parrot[0:6]) # 0 is the very first character and 6 is the length of the string parrot. Result = "Lemond"
print(parrot[-5]) #-1 is the address of last character i.e 'i'. Result = "w"

#for 0 and 6, the meanings are same, and 2 means escaping a single character. Result = "Lmn"
print(parrot[0:6:2])

number = "1,223,334,445,556,667"
print(number[1::4]) #leaving blank means it is 0
numbers = "1, 2, 3, 4, 5"
print(numbers[::3])
stmt1 = "Gotamey is "
stmt2 = "Dancing\t"
print(stmt1 + stmt2)
print(stmt2 *4) # *4 Multiplies the string for 4 times

# print(stmt2 *4 + 8) is incorrect, it gives error but
print(stmt2 *(4+8))
