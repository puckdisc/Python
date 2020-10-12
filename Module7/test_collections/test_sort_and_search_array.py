import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array


class MyTestCase(unittest.TestCase):

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_search_array_valid_single(self, input):
        self.assertEqual(sort_and_search_array.search_array(9), 1)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_search_array_invalid(self, input):
        self.assertEqual(sort_and_search_array.search_array(16), -1)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_sort_array1(self, input):
        self.assertEqual(sort_and_search_array.sort_array(), [9, 11, 45])

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 11, 1])
    def test_sort_array2(self, input):
        self.assertEqual(sort_and_search_array.sort_array(), [1, 11, 11])

if __name__ == '__main__':
    unittest.main()
