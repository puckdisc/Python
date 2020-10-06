import unittest
from more_fuctions import validate_input_in_fuctions


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        with self.assertRaises(TypeError):
            validate_input_in_fuctions.score_input()

    def test_score_input_test_score_valid(self):
        self.assertEqual(True, validate_input_in_fuctions.score_input('abc', 50))

    def test_score_input_test_score_below_range(self):
        self.assertEqual(False, validate_input_in_fuctions.score_input('abc', -10))

    def test_score_input_test_score_above_range(self):
        self.assertEqual(False, validate_input_in_fuctions.score_input('abc', 105))

    def test_score_input_test_score_non_numeric(self):
        with self.assertRaises(TypeError):
            validate_input_in_fuctions.score_input('abc', 'abc')

    def test_score_input_invalid_message(self):
        self.assertEqual(True, validate_input_in_fuctions.score_input('abc', 50, 'passed into argument'))


if __name__ == '__main__':
    unittest.main()
