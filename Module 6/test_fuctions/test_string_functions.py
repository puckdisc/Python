import unittest
from more_fuctions import string_functions


class MyTestCase(unittest.TestCase):
    """verify expected string product return"""
    def test_multiple_strings(self):
        """test parameters"""
        message = 'abc'
        n = 2

        self.assertEqual('abcabc', string_functions.multiply_string(message, n))


if __name__ == '__main__':
    unittest.main()
