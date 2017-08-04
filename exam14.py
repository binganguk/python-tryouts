"""
Task 1
======

Imagine you work in a vegetable shop. You are a programmer.

Carrots are priced as high as 10 euro per kilogram.

All carrots are orange. Prices are vast.

Weights (are given in kilograms) do vary from one carrot to another (are given in the constructor).

Make a function/method (`get_price` ) which calculates the price of the carrot.

Make the following cases:

    weight of a carrot is 500 grams
    weight of a carrot is 200 grams
    weight of a carrot is 100 grams
    weight of a carrot is 2 kilograms

Task 2
======

When you print a Carrot object you should get the following information:

    Carrot, weight ??? kilograms, price ??? $.

Task 3
======

Do the same for potatoes.

    Potato, weight ??? kilograms, price ??? $.
"""

class Vegetable(object):
    name = None
    weight = None
    color = None
    price_per_kilo = None

    def __repr__(self):
        return "{0}, weight {1} kilograms, price {2} $".format(self.name, self.weight, self.get_price())

    def __init__(self, weight):
        self.weight = weight

    def get_price(self):
        return self.weight * self.price_per_kilo


class Carrot(Vegetable):
    name = "Carrot"
    weight = None
    color = "orange"
    price_per_kilo = 2


class Potato(Vegetable):
    name = "Potato"
    weight = None
    color = "yellow"
    price_per_kilo = 10


c1 = Carrot(weight=0.5)
c2 = Carrot(weight=0.2)
c3 = Carrot(weight=0.1)
c4 = Carrot(weight=2)

print c1.get_price()
print c1

print c2.get_price()
print c2

print c3.get_price()
print c3

print c4.get_price()
print c4

p1 = Potato(weight=0.5)
p2 = Potato(weight=0.2)
p3 = Potato(weight=0.1)
p4 = Potato(weight=2)

print p1.get_price()
print p1

print p2.get_price()
print p2

print p3.get_price()
print p3

print p4.get_price()
print p4
