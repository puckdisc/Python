import unittest
from more_fuctions import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiple_strings(self):
        message = 'abc'
        self.assertEqual('abc', string_functions.multiply_string(message, 1))
        self.assertEqual('abcabcabcabc', string_functions.multiply_string(message, 4))


if __name__ == '__main__':
    unittest.main()
