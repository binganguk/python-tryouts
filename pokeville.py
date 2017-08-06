"""

Task 1
======

Implement upgrades.

    Initial: Bulbasaur
    Upgrade: Ivysaur
    Upgrade: Venusaur

Rules:

- Each pokemon has vast amount of immutable properties/fields, such as name, fast_attack, charged_attack.
- In addition to the immutable properties/fields, they have a number of customisable properties/fields, such as
  custom_name, number_of_candies, amount_of_stardust.
- All customisable fields are optional, and shall be passed as additional constructor arguments.

For example:

b = Bulbasaur(custom_name="Tigran")

Each pokemon shall have the following methods:

- give_candy: for the first power-up you need 2 candies, for the second - 4 candies, for the third - 8 candies (and
  so on).
- give_stardust: For the first power-up you need 5 stardust, for the second you need 25, for the third you need 125
  stardust (and so on).
- power_up: Combat power starts with 20 (initial 10 + 10 power of 1), after power up it becomes 110 (initial 10 + 10
  power of 2), then 1010 (initial 10 + 10 power of 3) and so on.

You should:

- Implement pokemon upgrades.
- Vast fields should not be preserved.
- Customisable fields shall be preserved.

It should finally work as follows:

b = Bulbasaur()
print b  # Should print something like Bulbasaur: 5 candies, 100 stardust, 200 combat power
b.give_candy(5)
b.give_stardust(10)
b.power_up()
b = b.upgrade()
print b  # Should print something like Ivysaur: 5 candies, 100 stardust, 10000 combat power

"""
class Pokemon(object):
    name = None
    custom_name = None
    number_of_candies = 0
    amount_of_stardust = 0
    power_up_counter = 1
    initial_combat_power = None
    combat_power_value = None
    fast_attack = None
    charged_attack = None

    def __init__(self, custom_name):
        self.custom_name = custom_name

    def __repr__(self):
        return "{0}: {1} candies, {2} stardust, {3} combat power".format(self.name,
                                                                         self.number_of_candies,
                                                                         self.amount_of_stardust,
                                                                         self.get_combat_power())

    def has_enought_candies_for_power_up(self):
        ""

    def has_enought_stardust_for_power_up(self):
        ""

    def get_combat_power(self):
        return self.initial_combat_power + self.combat_power_value ** self.power_up_counter

    def upgrade(self):
        ""

    def give_candy(self, number):
        self.number_of_candies += number

    def give_stardust(self, amount):
        self.amount_of_stardust += amount


class Bulbasaur(Pokemon):
    name = "Bulbasaur"
    initial_combat_power = 10
    combat_power_value = 10
    fast_attack = 12
    charged_attack = 55


class Ivysaur(Pokemon):
    name = "Ivysaur"
    initial_combat_power = 100
    combat_power_value = 10
    fast_attack = 15
    charged_attack = 70


z = Bulbasaur(custom_name="Tigran")
print z
z.give_candy(5)
z.give_stardust(10)
print z
print z.get_combat_power()
