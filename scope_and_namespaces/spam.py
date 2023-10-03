def spam1():
    def spam2():
        def spam3():
            z = " even more spam"
            z += y
            print("In spam2, locals are {}".format(locals()))
            return z

        y = " more " + x # y must exist before spam3 is called
        y += spam3() # do not combine these assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam" # x must exist before spam2 is called
    x += spam2() # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
