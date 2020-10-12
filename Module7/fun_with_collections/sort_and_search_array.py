from array import array as arr
from fun_with_collections import basic_list_exception


def search_array(search):

    """
    Searches array for value and returns index

    Calls basic_list.make_list() and accepts list return. Converts list to
    signed integer array. Takes param search and returns index or -1
    if not found.


    :param search: integer to search for
    :return: search_index: integer index of search
    """

    fun_list = basic_list_exception.make_list()
    fun_array = arr('i', fun_list)
    try:
        search_index = fun_array.index(search)
        print(str(search) + ' is at ' + str(search_index))
        return search_index
    except ValueError:
        return -1


def sort_array():
    pass


if __name__ == '__main__':
    search_array(6)
