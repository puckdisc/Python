import unittest
from unittest.mock import patch
from fun_with_collections import search_and_sort_list


class MyTestCase(unittest.TestCase):

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_sort_list(self, input):
        self.assertEqual(search_and_sort_list.sort_list(), [9, 11, 45])

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_search_list_valid_single(self, input):
        self.assertEqual(search_and_sort_list.search_list(9), 1)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_search_list_invalid(self, input):
        self.assertEqual(search_and_sort_list.search_list(16), -1)

if __name__ == '__main__':
    unittest.main()
