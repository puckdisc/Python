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
    # Call for list
    fun_list = basic_list_exception.make_list()
    fun_array = arr('i', fun_list)

    # Search for index of search value
    try:
        search_index = fun_array.index(search)
        print(str(search) + ' is at ' + str(search_index))
        return search_index
    except ValueError:
        return -1


def sort_array():

    """
    Sorts array

    Calls basic_list_exception.make_list. Converts integer list to integer array. Sorts array
    with a loop. Returns copy of sorted array list

    :return: return_list: copy of sorted array list
    """
    # Call for list and convert to array
    return_list = []
    fun_list = basic_list_exception.make_list()
    fun_array = arr('i', fun_list)

    # Sort array
    for x in range(0, len(fun_array)):
        for y in range(x+1, len(fun_array)):
            if fun_array[x] > fun_array[y]:
                temp = fun_array[x]
                fun_array[x] = fun_array[y]
                fun_array[y] = temp
        return_list.append(fun_array[x])

    # Returning a copy of the sorted array list because it satisfies the test. Return requirements
    # were not provided so I just returned a list.
    return return_list


if __name__ == '__main__':
    sort_array()
