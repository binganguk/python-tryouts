import unittest

from characters import *


class CharactersTestCase(unittest.TestCase):

    def test_give_candy(self):
        z = Bulbasaur(custom_name="Tigran")

        # First time
        self.assertEqual(
            z.give_candy(39),
            'Thank you! Now I have 39 candies.'
        )
        self.assertEqual(39, z.number_of_candies)

        # Second time
        self.assertEqual(
            z.give_candy(11),
            'Thank you! Now I have 50 candies.'
        )
        self.assertEqual(50, z.number_of_candies)

    def test_give_stardust(self):
        z = Bulbasaur(custom_name="Tigran")

        # first time
        self.assertEqual(
            z.give_stardust(39),
            'Thank you! Now I have 39 stardust.'
        )
        self.assertEqual(39, z.amount_of_stardust)

        # second time
        self.assertEqual(
            z.give_stardust(98),
            'Thank you! Now I have 137 stardust.'
        )
        self.assertEqual(137, z.amount_of_stardust)

    def test_has_enough_candies_for_power_up(self):
        z = Bulbasaur(custom_name="Tigran")

        # False case
        self.assertEqual(False, z.has_enough_candies_for_power_up())

        # True case
        z.give_candy(3)
        self.assertEqual(True, z.has_enough_candies_for_power_up())

        # False case
        z.give_stardust(30)
        z.power_up()
        self.assertEqual(False, z.has_enough_candies_for_power_up())

        # True case
        z.give_candy(3)
        self.assertEqual(True, z.has_enough_candies_for_power_up())


    def test_has_enough_stardust_for_power_up(self):
        z = Bulbasaur(custom_name="Tigran")

        # False case
        self.assertEqual(False, z.has_enough_stardust_for_power_up())

        # True case
        z.give_stardust(5)
        self.assertEqual(True, z.has_enough_stardust_for_power_up())

        # False case
        z.give_candy(500)
        z.power_up()
        self.assertEqual(False, z.has_enough_stardust_for_power_up())

        # True case
        z.give_stardust(33)
        self.assertEqual(True, z.has_enough_stardust_for_power_up())

    def test_candies_needed_for_next_power_up(self):
        z = Bulbasaur(custom_name="Tigran")

        # first level
        self.assertEqual(2, z.candies_needed_for_next_power_up())

        # second level
        z.give_candy(5)
        z.give_stardust(30)
        z.power_up()
        self.assertEqual(4, z.candies_needed_for_next_power_up())

    def test_stardust_needed_for_next_power_up(self):
        z = Bulbasaur(custom_name="Tigran")

        # first level
        self.assertEqual(5, z.stardust_needed_for_next_power_up())

        # second level
        z.give_candy(5)
        z.give_stardust(30)
        z.power_up()
        self.assertEqual(25, z.stardust_needed_for_next_power_up())


unittest.main()
