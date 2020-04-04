# tet = open("something.txt", 'r')
#
# for line in tet:
#
#
#     print(line)
#
# tet.close()


#
# with open("something.txt",'r') as tet: #this literally means that --- tet = open("something.txt", 'r')
#     for line in tet:
#         # print(line)
#         if "disease" in line.lower():  #yedi euta line maa katai pani "disease" vanni word xa vaney
#             print(line, end='')    #print garna paryo hai guyz


# with open("something.txt",'r') as tet:
#     # line = tet.readline()
#     # print(line) # It prints only one line
#     print("*" * 40)
#
#     lines = tet.readlines()  #It prints all the lines in a same line,,, Or in a list like ['a','b',....]
#     print(lines)
#
#     for line in lines: #List ko single single value lai print garxa hai guyz,,, line nalekhera gotamey lekheni aauni result tei ho
#         print("\n")
#         print(line, end='')
#



with open("something.txt", 'r') as tet:
    line = tet.read() #Purai .txt file xai line wise print huna dinxa tet.read() le, tet.readline() le only one line
    print(line)

    for lines in line[::-1]: #Suraj lai jaruS garera print garnako lagi dinxa
        print(lines, end='')