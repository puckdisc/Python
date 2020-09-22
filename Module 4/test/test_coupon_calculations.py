# Sean Gilbert
# CIS 189 Fall 2020
# Module 4 Topic 3
# Unit tests of coupon_calculations.py


import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        price = 8
        self.assertAlmostEqual(8.81, coupon_calculations.calculate_order(price, 5, 0.1), 2)
        self.assertAlmostEqual(8.65, coupon_calculations.calculate_order(price, 5, 0.15), 2)
        self.assertAlmostEqual(8.49, coupon_calculations.calculate_order(price, 5, 0.2), 2)
        self.assertAlmostEqual(5.95, coupon_calculations.calculate_order(price, 10, 0.1), 2)
        self.assertAlmostEqual(5.95, coupon_calculations.calculate_order(price, 10, 0.15), 2)
        self.assertAlmostEqual(5.95, coupon_calculations.calculate_order(price, 10, 0.2), 2)

    def test_price_under_between_ten_thirty(self):
        price = 22
        self.assertAlmostEqual(24.168, coupon_calculations.calculate_order(price, 5, 0.1), 2)
        self.assertAlmostEqual(23.267, coupon_calculations.calculate_order(price, 5, 0.15), 2)
        self.assertAlmostEqual(22.366, coupon_calculations.calculate_order(price, 5, 0.20), 2)
        self.assertAlmostEqual(19.398, coupon_calculations.calculate_order(price, 10, 0.1), 2)
        self.assertAlmostEqual(18.762, coupon_calculations.calculate_order(price, 10, 0.15), 2)
        self.assertAlmostEqual(18.126, coupon_calculations.calculate_order(price, 10, 0.2), 2)

    def test_price_under_between_thirty_fifty(self):
        price = 39
        self.assertAlmostEqual(44.386, coupon_calculations.calculate_order(price, 5, 0.1), 2)
        self.assertAlmostEqual(42.584, coupon_calculations.calculate_order(price, 5, 0.15), 2)
        self.assertAlmostEqual(40.782, coupon_calculations.calculate_order(price, 5, 0.20), 2)
        self.assertAlmostEqual(39.616, coupon_calculations.calculate_order(price, 10, 0.1), 2)
        self.assertAlmostEqual(38.079, coupon_calculations.calculate_order(price, 10, 0.15), 2)
        self.assertAlmostEqual(36.542, coupon_calculations.calculate_order(price, 10, 0.2), 2)

    def test_price_equal_over_fifty(self):
        price = 66
        self.assertAlmostEqual(58.194, coupon_calculations.calculate_order(price, 5, 0.1), 2)
        self.assertAlmostEqual(54.961, coupon_calculations.calculate_order(price, 5, 0.15), 2)
        self.assertAlmostEqual(51.728, coupon_calculations.calculate_order(price, 5, 0.20), 2)
        self.assertAlmostEqual(53.424, coupon_calculations.calculate_order(price, 10, 0.1), 2)
        self.assertAlmostEqual(50.456, coupon_calculations.calculate_order(price, 10, 0.15), 2)
        self.assertAlmostEqual(47.488, coupon_calculations.calculate_order(price, 10, 0.2), 2)


if __name__ == '__main__':
    unittest.main()
