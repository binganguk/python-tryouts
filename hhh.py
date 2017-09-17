def plus(lo, li, lu):
    return lo + li +lu

print(plus(64, 65, 66))

class School(object):
    name = None
    address = None
    start_date = None
    max_students = None

    def about(self):
        if self.start_date < 1930:
            print "its a wonder that the {0} isn't bombed yet".format(self.name)
        else:
            print "{0} is a new school".format(self.name)

        if self.max_students >= 2000:
            print "boom!(the school exploded because of too many students)"

class Hogwarts(School):
    name =  "Hogwarts"
    address = "not found"
    max_students = 5000
    start_date = 1

class Preadinius(School):
    name = "Preadinius"
    address = "not found"
    max_students = 1000
    start_date = 1947

h = Hogwarts()
h.about()

p = Preadinius()
p.about()

