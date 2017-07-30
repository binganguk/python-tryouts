#!/usr/bin/env python
"""
Task
====

Make 2 classes:

    - White dragon
    - Red dragon

The name of the white dragon is White dragon
The name of the red dragon is Red dragon

Both dragons can say hello (class method/function `hello`). When they say hello, they say it as follows:

    - Hello, my name is ... (the name of the dragon). What a nice day for growling, isn't it? Grr...

After declaring the classes, make two objects/instances (one of each) and say hello.
"""

class Dragon():

    name = None
    color = None

    def say_hello(self):
        print "Hello, my name is {0}. What a nice day for growling, isn't it? Grr...".format(self.name)


class WhiteDragon(Dragon):

    name = "White dragon"
    color = "white"


class RedDragon(Dragon):

    name = "Red dragon"
    color = "red"


r = RedDragon()

w = WhiteDragon()

r.say_hello()

w.say_hello()
