from fun_with_collections import basic_list_exception


def sort_list():

    """
    Sorts list

    Calls basic_list_exception.make_list(). The return is assigned variable name
    fun_list. Fun_list is sorted and returned.

    :return: fun_list: sorted list
    """
    fun_list = basic_list_exception.make_list()
    fun_list.sort()
    return fun_list


def search_list(search):
    """
    Returns the index of the desired list item

    Calls basic_list_exception.make_list(). This return is assigned variable name
    fun_list. Parameter 'search' is searched for in fun_list and the index returned.
    An invalid search will return -1. This function will only return the first occurrence
    of the desired item. Multiple occurrences are not accounted for.


    :param search: integer to search for
    :return: location: integer index of desired search in fun_list
    """
    fun_list = basic_list_exception.make_list()
    for x in range(len(fun_list)):
        try:
            location = fun_list.index(search)
            return location
        except ValueError:
            return -1


if __name__ == '__main__':
    search_list(2)
