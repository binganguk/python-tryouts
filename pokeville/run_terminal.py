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

from characters import *


# Bulbasaur

z = Bulbasaur(custom_name="Tigran")
print z

# Give some candies and stardust
print z.give_candy(5)
print z.give_stardust(10)
print z
print z.power_up()
print z
print z.get_combat_power()

# Try to upgrade. This should fail.
z = z.upgrade()

# Give some candies for upgrade.
print z.give_candy(800)
print z.give_stardust(1000)

# Upgrade to Ivysaur
z = z.upgrade()
print z

print z.power_up()
print z

print z.power_up()
print z

# Upgrade to Venusaur
z = z.upgrade()
print z

print z.power_up()
print z

print z.power_up()
print z

print z.power_up()
print z

print z.power_up()
print z

print z.power_up()
print z

print z.power_up()
print z

print z.power_up()
print z

print z.power_up()
print z
