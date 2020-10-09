def make_list():
    """
    Adds get_input() return to list

    :return: integer list
    """
    fun_list = []

    try:
        for x in range(3):
            var = get_input()

            if var.isnumeric() is False:
                raise ValueError('Non-integer input detected!!!1!11!')

            var = int(var)
            fun_list.append(var)

            if fun_list[x] < 1:
                raise ValueError('Entry less than 1')
            if fun_list[x] >= 51:
                raise ValueError('Entry more than 50')
            print(fun_list[x])

        print(fun_list)
        return fun_list

    except ValueError:
        raise


def get_input():
    """
    returns a user-defined string

    :return: string
    """
    user_input = input('Enter an integer: ')
    return user_input


if __name__ == '__main__':
    make_list()
