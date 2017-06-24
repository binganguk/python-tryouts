def harik(x, y):
    return x+y

print harik(12, 87)
print harik(34, 85)


def toe(x, y):
    return x - y


print toe(100, 20)


def piep(a,b,c):
    return a+b+c


print piep (45, 28, 97)


def say_good_morning(free_from_work, number_of_children, children_are_very_stubborn):
    text = ""
    if free_from_work is True:

        if children_are_very_stubborn and number_of_children > 10:
            text += "; one pack isn't enough, get 20 and don't use to make explosion, but rather use it for the purpose!"
        else:
            text += "play some games with children,then go to the shop,buy some candies and use it together to make a cola mentos explosion"
    else:
        text += "make sure not to be late at work"

    return text


print say_good_morning(True, 9, False)
print say_good_morning(True, 19, True)
print say_good_morning(False, 11, True)

x = raw_input()
print x * 4


