import unittest
from main import camper_age_input

class MyTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(240, camper_age_input.convert_to_months(20))


if __name__ == '__main__':
    unittest.main()
