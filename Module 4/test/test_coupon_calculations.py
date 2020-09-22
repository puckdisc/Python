import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        price = 8
        self.assertAlmostEqual(8.65,coupon_calculations.calculate_price(price, 5, 0.1),3)
        self.assertAlmostEqual(8.5,coupon_calculations.calculate_price(price, 5, 0.15),3)
        self.assertAlmostEqual(8.35,coupon_calculations.calculate_price(price, 5, 0.2),3)
        self.assertAlmostEqual(0,coupon_calculations.calculate_price(price, 10, 0.1),3)
        self.assertAlmostEqual(0,coupon_calculations.calculate_price(price, 10, 0.15),3)
        self.assertAlmostEqual(0,coupon_calculations.calculate_price(price, 10, 0.2),3)


if __name__ == '__main__':
    unittest.main()
