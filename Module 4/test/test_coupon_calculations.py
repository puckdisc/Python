import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        price = 8
        self.assertAlmostEqual(8.81,coupon_calculations.calculate_order(price, 5, 0.1),2)
        self.assertAlmostEqual(8.65,coupon_calculations.calculate_order(price, 5, 0.15),2)
        self.assertAlmostEqual(8.49,coupon_calculations.calculate_order(price, 5, 0.2),2)
        self.assertAlmostEqual(5.95,coupon_calculations.calculate_order(price, 10, 0.1),2)
        self.assertAlmostEqual(5.95,coupon_calculations.calculate_order(price, 10, 0.15),2)
        self.assertAlmostEqual(5.95,coupon_calculations.calculate_order(price, 10, 0.2),2)

    def test_price_under_between_ten_thirty(self):
        price = 22
        self.assertAlmostEqual(22, coupon_calculations.calculate_order(price, 5, 0.1),2)
        self.assertAlmostEqual(22, coupon_calculations.calculate_order(price, 5, 0.15),2)
        self.assertAlmostEqual(22, coupon_calculations.calculate_order(price, 5, 0.20),2)
        self.assertAlmostEqual(22, coupon_calculations.calculate_order(price, 10, 0.1),2)
        self.assertAlmostEqual(22, coupon_calculations.calculate_order(price, 10, 0.15),2)
        self.assertAlmostEqual(22, coupon_calculations.calculate_order(price, 10, 0.2),2)


if __name__ == '__main__':
    unittest.main()
