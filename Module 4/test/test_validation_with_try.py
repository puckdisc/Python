# Sean Gilbert
# CIS 189 Fall 2020
# unit test input validation

import unittest
from input_validation import validation_with_try


class MyTestCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, 78)

        with self.assertRaises(ValueError):
            validation_with_try.average(90, -89, 78)



if __name__ == '__main__':
    unittest.main()
