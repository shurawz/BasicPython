# # def function_call():
# #
# #     width= 90
# #     name = "Gotamey is life"
# #     difference = width = len(name)
# #     print(" " * difference + name)
# #
# # #call the function
# # function_call()
#
# def function_text(*args): # '*' means there can be any number of arguments.
#     text = ""
#     for arg in args: # for item in list type,
#         text += str(arg) + " " # If this line doesnot contain str() then it will be error because (In line 15)
#         #arguments is int value and str makes anything as string.
#     diff = 80 - len(text)
#     print(" " * diff, text)
#
# # calling of function_
#
# function_text("Suraj","Gotamey", 23, 45, "How")
# function_text("Suraj Gotamey")
# # function_text("Suraj Gotamey is hero hai guyz. Don't misunderstand me.")


def centered_file(*args, sep=' '):
    text = ""
    for arg in args:
        text = text + str(arg) + sep
    m_argin = (80 - len(text))
    return " " * m_argin + text

with open("menu", 'w') as menu:
    print(centered_file("Spam and eggs"), file=menu)
    s1 = centered_file("Timri aama ko xoro hau timi")
    print(s1, file=menu)
    print(centered_file("Spam spam and eggs"), file=menu)
    print(centered_file("Spam spam spam and eggs"), file=menu)
    print(centered_file("Suraj", "Gotamey", 12, 45, "Love"), file=menu)

    print("=" + str(12 * 4))
    print(sorted(["o", "b", "x", "a "]))
