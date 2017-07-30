class VolkswagenGolf1(object):
    name = "Volkswagen golf 1"
    color = "White"
    max_speed = 200
    durability = 1000

    def print_name(self):
        print self.name

    def drive(self, speed):
        print "Driving {0} tutu, max speed {1}, durability {2}".format(speed, self.max_speed, self.durability)

    def print_color(self):
        print "Color {0}".format(self.color)

    def print_durability(self):
        print "{0}".format(self.durability)


v1 = VolkswagenGolf1()
v2 = VolkswagenGolf1()
v3 = VolkswagenGolf1()
v4 = VolkswagenGolf1()


v1.name
v2.name
v3.name
v4.name

v1.print_name()  # self == v1

v2.print_name()  # self == v2

v1.drive(3)  # self == v1, km == 3

v2.drive(5)  # self == v2, km == 5 max speed == 200

v3.print_name()  # self == v3

v4.print_name()  # self == v4

v1.color
v1.max_speed
v1.durability

v3.max_speed
v3.durability

v4.color

