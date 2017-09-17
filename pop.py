def big(a, b):
    if a > b:
        return a
    else:
        return b

def small(a, b):
    if a < b:
        return a
    else:
        return b

def minimum(a, b, c):

    if a > b < c:
        return b
    if c > b < a:
        return b

    if b > a < c:
        return a
    if c > a < b:
        return a

    if a > c < b:
        return c
    if b > c < a:
        return c


def medium(a, b, c):


    if a < b < c:
        return b
    if c > b > a:
        return b

    if b > a > c:
        return a
    if c > a > b:
        return a

    if a > c > b:
        return c
    if a < c < b:
        return c



# print big(5, 8)
# print big(8, 5)
# print small(9, 3)
# print small(3, 9)
print medium(2, 6, 9)
print medium(11, 6, 9)
print medium(11, 12, 9)
print medium(11, 12, 14)
