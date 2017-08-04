"""
Task 1
======

Imagine you work in a vegetable shop. You are a programmer.

Cucumbers are priced as high as 10 euro per kilogram.

All cucumbers are green. Prices are vast.

Weights (are given in kilograms) do vary from one cucumber to another (are given in the constructor).

Make a function/method (`get_price` ) which calculates the price of the cucumber.

Make the following cases:

    weight of a cucumber is 500 grams
    weight of a cucumber is 200 grams
    weight of a cucumber is 100 grams
    weight of a cucumber is 2 kilograms

Task 2
======

When you print a Cucumber object you should get the following information:

    Cucumber, weight ??? kilograms, price ??? $.
"""


class Cucumber(object):
    name = "Cucumber"
    color = "green"
    weight = None
    price_per_kilo = 10  # Prices are in euro

    def __repr__(self):
        return "Cucumber, weight {0} kilograms, price {1} $".format(self.weight, self.get_price())

    def __init__(self, weight):
        self.weight = weight

    def get_price(self):
        return self.weight * self.price_per_kilo


c1 = Cucumber(0.5)
c2 = Cucumber(0.2)
c3 = Cucumber(0.1)
c4 = Cucumber(2)

print c1.get_price()
print c2.get_price()
print c3.get_price()
print c4.get_price()

print c1
print c2
print c3
print c4
