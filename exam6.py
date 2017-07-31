"""
There are two sheep.

    - White sheep
    - Black sheep

Both of them can say "baa", thus, declare a function/method say_baa. The name of the white sheep is White sheep.
The name of the black sheep is Black sheep. Make another function called say_name. It should print the following:

    Hello, my name is ... (name of the sheep).

After declaring classes, make two objects: w and b. Make both of the sheep say baa and their names.
"""

class Sheep(object):

    name = None
    color = None

    def say_name(self):
        print "Hello, my name is {0}".format(self.name)

    def say_baa(self):
        print "baa"


class BlackSheep(Sheep):
    name = "Black sheep"
    color = "black"


class WhiteSheep(Sheep):
    name = "White sheep"
    color = "white"


b = BlackSheep()

w = WhiteSheep()

b.say_name()
b.say_baa()

w.say_name()
w.say_baa()
