import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array


class MyTestCase(unittest.TestCase):

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_search_list_valid_single(self, input):
        self.assertEqual(sort_and_search_array.search_array(9), 1)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[11, 9, 45])
    def test_search_list_invalid(self, input):
        self.assertEqual(sort_and_search_array.search_array(16), -1)

if __name__ == '__main__':
    unittest.main()
