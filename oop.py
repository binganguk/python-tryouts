"""
Object oriented programming.
"""


def bla():
    """The `bla` function."""


# `my_bla` variable.
my_bla = bla()


class Pokemon(object):
    """Base class for pokemon's classification."""

    # `my_something` property.
    my_something = 3

    def something(self):
        """The `something` method."""


# Initialize the class
pokemon = Pokemon()

pokemon.something()  # Calling the `something` method

print pokemon.my_something
