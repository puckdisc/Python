def make_list():
    """
    calls get_input(), appends return to list,
    converts appendage to integer, returns integer list

    :return: integer list
    """
    fun_list = []

    try:
        for x in range(3):
            var = [get_input()]
            fun_list[len(fun_list):] = var
            fun_list[x] = int(fun_list[x])

        print(fun_list)
        return fun_list

    except ValueError:
        print('Non-integer input detected!!!1!11!')


def get_input():
    """
    returns a user-defined string

    :return: string
    """
    user_input = input('Enter an integer: ')
    return user_input


if __name__ == '__main__':
    make_list()
