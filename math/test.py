import unittest

from functions import *


class FunctionsTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(
            sum(3, 4),
            7
        )
        self.assertEqual(
            sum(5, 10),
            15
        )

    def test_mult(self):
        self.assertEqual(
            mult(3, 4),
            12
        )


unittest.main()
