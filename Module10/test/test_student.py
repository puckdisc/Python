import unittest
from class_definitions import student as s

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Ovechkin', 'Alex', 'Goal Scoring', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Alex')
        self.assertEqual(self.student.last_name, 'Ovechkin')
        self.assertEqual(self.student.major, 'Goal Scoring')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.first_name, 'Alex')
        self.assertEqual(self.student.last_name, 'Ovechkin')
        self.assertEqual(self.student.major, 'Goal Scoring')
        self.assertEqual(self.student.gpa, 4.0)

if __name__ == '__main__':
    unittest.main()
