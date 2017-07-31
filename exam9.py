"""
Declare a function which is called `decrease`, which takes 1 argument/parameter. The `decrease` function should
repeatedly decrease the given value by 3, until the value gets lower than 11. You should print the result.

Call your decrease function with the following arguments:

    611
    818
    74
"""
def decrease(value):
    while value >= 11:
        value -= 3

    return value

print decrease(611)

print decrease(818)

print decrease(74)

print decrease(612)