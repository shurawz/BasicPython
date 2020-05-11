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


class Mallard(Duck):
    pass


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Mah pengium hidna sakxu")

    def swim(self):
        print("Mah dhukka paudina sakxu")

    def sound(self):
        print("Halka aawaz ni nikalna sakxu")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # if isinstance(duck, Duck):
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a "+str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate") # TODO remove this before release
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    trump = Duck()
    trump.fly()
