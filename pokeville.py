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
    number_of_candies_required_for_upgrade = None
    upgrade_class = None

    def __init__(self, custom_name=None, number_of_candies=0, amount_of_stardust=0):
        self.custom_name = custom_name
        self.number_of_candies = number_of_candies
        self.amount_of_stardust = amount_of_stardust

    def __repr__(self):
        return "{0}: {1} candies, {2} stardust, {3} combat power, level {4}".format(
            self.name,
            self.number_of_candies,
            self.amount_of_stardust,
            self.get_combat_power(),
            self.power_up_counter
        )

    def has_enough_candies_for_power_up(self):
        """Check if pokemon has enough candies for a power-up.

        For the first power-up you need 2 candies, for the second - 4 candies, for the third - 8 candies (and so on).

            1 level == 2 candies (2 ** 1)
            2 level == 4 candies (2 ** 2)
            3 level == 8 candies (2 ** 3)
            4 level == 16 candies (2 ** 4)
            n level == ? candies (2 ** n)

        :return:
        """
        if self.number_of_candies >= 2 ** self.power_up_counter:
            return True
        else:
            return False

    def has_enough_stardust_for_power_up(self):
        """Check if pokemon has enough stardust for a power-up.

        For the first power-up you need 5 stardust, for the second you need 25, for the third you need 125 (and so on).

            1 level == 5 stardust (5 ** 1)
            2 level == 25 stardust (5 ** 2)
            3 level == 125 stardust (5 ** 3)
            4 level == 625 stardust (5 ** 4)
            n level == ? stardust (5 ** n)

        :return:
        """
        if self.amount_of_stardust >= 5 ** self.power_up_counter:
            return True
        else:
            return False

    def power_up(self):
        if self.has_enough_candies_for_power_up() and self.has_enough_stardust_for_power_up():
            self.number_of_candies -= 2 ** self.power_up_counter
            self.amount_of_stardust -= 5 ** self.power_up_counter
            self.power_up_counter += 1
            return True
        else:
            return False

    def get_combat_power(self):
        return self.initial_combat_power + self.combat_power_value ** self.power_up_counter

    def upgrade(self):
        """"""
        if self.number_of_candies_required_for_upgrade and self.number_of_candies >= self.number_of_candies_required_for_upgrade:
            self.number_of_candies -= self.number_of_candies_required_for_upgrade
            return self.upgrade_class(
                custom_name = self.custom_name,
                number_of_candies = self.number_of_candies,
                amount_of_stardust = self.amount_of_stardust
            )
        else:
            return self

    def give_candy(self, number):
        """Give X number of candies to pokemon.

        Pokemon should reply: "Thank you! Now I have ? candies."
        """
        self.number_of_candies += number
        return "Thank you! Now I have {0} candies.".format(self.number_of_candies)

    def give_stardust(self, amount):
        self.amount_of_stardust += amount
        return "Thank you! Now I have {0} stardust.".format(self.amount_of_stardust)


class Venusaur(Pokemon):
    name = "Venusaur"
    initial_combat_power = 1000
    combat_power_value = 10
    fast_attack = 20
    charged_attack = 180


class Ivysaur(Pokemon):
    name = "Ivysaur"
    initial_combat_power = 100
    combat_power_value = 10
    fast_attack = 15
    charged_attack = 70
    number_of_candies_required_for_upgrade = 600
    upgrade_class = Venusaur


class Bulbasaur(Pokemon):
    name = "Bulbasaur"
    initial_combat_power = 10
    combat_power_value = 10
    fast_attack = 12
    charged_attack = 55
    number_of_candies_required_for_upgrade = 150
    upgrade_class = Ivysaur


z = Bulbasaur(custom_name="Tigran")
print z
print z.give_candy(5)
print z.give_stardust(10)
print z
print z.power_up()
print z
print z.get_combat_power()
z = z.upgrade()

print z.give_candy(800)

z = z.upgrade()
print z
