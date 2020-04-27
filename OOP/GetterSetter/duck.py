class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, it is fun.")
        elif self.ratio == 1:
            print("It's hard but I'm flying.")
        else:
            print("OK fine, I' walking.")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)
        # a underscore '_' before the variable indicates that the variable is for internsl use.
        # It is also known as 'weak private'.

    def walk(self):
        print("Hidd vaii hidd")

    def swim(self):
        print("Paudi vai paudi")

    def sound(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Mah pengium hidna sakxu")

    def swim(self):
        print("Mah dhukka paudina sakxu")

    def sound(self):
        print("Halka aawaz ni nikalna sakxu")

#
# def Bird(duck):
#     duck.walk()
#     duck.sound()
#     duck.swim()


if __name__ == '__main__':
    trump = Duck()
    trump.fly()



    # Bird(trump)
    #
    # paisa = Penguin()
    # Bird(paisa)