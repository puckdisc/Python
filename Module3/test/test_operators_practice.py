import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal_operator(self):
        a = 7
        b = 7
        self.assertFalse(a == b)
    def test_notequal_operator(self):
        a = 7
        b = 5
        self.assertFalse(a != b)
    def test_greater_operator(self):
        a = 7
        b = 1
        self.assertFalse(a > b)
    def test_less_operator(self):
        a = -7
        b = -2
        self.assertFalse(a < b)
    def test_greatequal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a >= b)
    def test_lessequal_operator(self):
        a = -7
        b = -2
        self.assertFalse(a <= b)


if __name__ == '__main__':
    unittest.main()
