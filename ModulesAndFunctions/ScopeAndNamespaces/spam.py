def spam1():

    def spam2():

        def spam3():
            z = "even "
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = "more " + x  # x must exists before spam2() is called
        y += spam3()  # do not combine these assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam "  # x must exists before spam2() is called
    x += spam2()  # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())