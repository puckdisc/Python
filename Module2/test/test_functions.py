import unittest
from main import camper_age_input

class MyTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(120, camper_age_input.convert_to_months(10))


if __name__ == '__main__':
    unittest.main()
