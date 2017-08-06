"""
Task 1
======

Imagine you work in a vegetable shop. You are a programmer.

Peppers are priced as high as 10 euro per kilogram.

All eggplants are dark blue. Prices are vast.

Weights (are given in kilograms) do vary from one pepper to another (are given in the constructor).

Make a function/method (`get_price` ) which calculates the price of the pepper.

Make the following cases:

    weight of a pepper is 500 grams
    weight of a pepper is 200 grams
    weight of a pepper is 100 grams
    weight of a pepper is 2 kilograms

Task 2
======

When you print a Pepper object you should get the following information:

    Pepper, weight ??? kilograms, price ??? $.

Task 3
======

Do the same for Eggplants.

    Pepper, weight ??? kilograms, price ??? $.
"""
class Vegetable(object):
    name = None
    color = None
    weight = None
    price_per_kilo = None

    def get_price(self):
        return self.price_per_kilo * self.weight

    def __init__(self, weight):
        self.weight = weight

    def __repr__(self):
        return "{0}, weight {1} kilo, price {2} $".format(self.name, self.weight, self.get_price())


class Pepper(Vegetable):
    name = "pepper"
    color = "red"
    weight = None
    price_per_kilo = 50


class Eggplant(Vegetable):
    name = "Eggplant"
    color = "black"
    weight = None
    price_per_kilo = 2


p1 = Pepper(0.5)

print p1.get_price()

print p1

e1 = Eggplant(200)

print e1.get_price()

print e1