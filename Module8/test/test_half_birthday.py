import unittest
import datetime
from more_fun_with_collections import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2015, 3, 15)
        self.assertEqual(datetime.datetime(2015, 9, 15), half_birthday.half_birthday(birthday))


if __name__ == '__main__':
    unittest.main()
