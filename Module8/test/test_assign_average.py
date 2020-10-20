import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_assign_average_A(self):
        self.assertEqual(90, assign_average.switch_average('A'))

    def test_assign_average_B(self):
        self.assertEqual(80, assign_average.switch_average('B'))

    def test_assign_average_C(self):
        self.assertEqual(70, assign_average.switch_average('C'))

    def test_assign_average_D(self):
        self.assertEqual(60, assign_average.switch_average('D'))

    def test_assign_average_F(self):
        self.assertEqual(0, assign_average.switch_average('F'))

    def test_assign_average_Z(self):
        self.assertEqual("Invalid Entry", assign_average.switch_average('S'))



if __name__ == '__main__':
    unittest.main()
