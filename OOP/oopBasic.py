class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.75)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 9.08
print(kenwood.price)

hamilton = Kettle("Hamilton", 8.75)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class. 
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

# print(Kettle.switch_on(kenwood)) it prints 'None'

print("=" * 80)

kenwood.power = 10
print(kenwood.power)

# print(hamilton.power) // It prints error or we can say program stops running at line49

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("\n")
print("Switching to atomic")
Kettle.power_source = "Atomic"
# if the value of global variable of class is changed whole methods gonna suffer it.
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("\n")
print("Switching to organic")
kenwood.power_source = "Organic"
# if the value of local variable is changed, only that local variable containing method gonna suffer it.
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
