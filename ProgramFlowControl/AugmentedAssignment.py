num = ("9,456,98,987,654,896")
cleanedNum = ''
for i in range(0,len(num)):
    if num[i] in '0123456789':
        cleanedNum += num[i]
newNum = int(cleanedNum)
print("The number is: {}".format(newNum))
