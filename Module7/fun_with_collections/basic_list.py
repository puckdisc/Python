def make_list():
    fun_list = []

    try:
        for x in range(3):
            var = [get_input()]
            fun_list[len(fun_list):] = var
            fun_list[x] = int(fun_list[x])

    except ValueError:
        print('Non-integer input detected!!!1!11!')

    print(fun_list)
    return fun_list


def get_input():
    pass

if __name__ == '__main__':
    make_list()
