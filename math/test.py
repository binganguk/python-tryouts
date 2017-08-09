import unittest

from functions import *


class FunctionsTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(
            first=sum(3, 4),
            second=7
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
    def test_min(self):
        self.assertEqual(

            min(56, 34),
            22
        )
unittest.main()
