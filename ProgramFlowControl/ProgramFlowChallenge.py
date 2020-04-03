# IpAddress = input("Enter the I.P Adddress")
# composed = ''
# count = 0
# segment = 0
# segLen = 0
#
# chall = IpAddress
#
# for i in range(0 , len(chall)):
#    if chall[i] in '0123456789':
#         composed = composed + chall[i]
#         if chall[i] == ".":
#             count = count
#         else:
#             count += 1
#
#
# print("The I.P Address is combined and resulted as: {}".format(composed))
# print("Numbers of number is:{}".format(count))

IpAdd = input("Enter your I.P Address")
segment = 1
segLen = 0

for i in range (0, len(IpAdd)):
    if IpAdd[i] == 0:
        print("Sorry bro, it is empty.")
    elif IpAdd[i] == '.':
        print("Segment {0} has {1} characters.".format(segment,segLen))
        segment += 1
        segLen = 0

    else:
        segLen += 1

print("Segment {0} has {1} characters.".format(segment,segLen))
print("Total Segments: {}".format(segment))

# google.github.io/styleguide/pyguide.html




