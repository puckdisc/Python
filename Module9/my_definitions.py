def greeting():
    # Prints greeting
    print('Greetings, friend!')


def author(code_author):
    # Prints the author
    print(code_author, 'is the author.')


def print_dict(fun_dict):
    # prints fun_dict line by line
    for key, value in fun_dict.items():
        print(key, 'are', value)


def print_set(fun_set):
    # prints fun_set line by line
    for x in fun_set:
        print(x)


if __name__ == '__main__':
    hockey_dict = {
        'Capitals': 'Cool',
        'Avalanche': 'Cool',
        'Blues': 'Cool',
        'Penguins': 'Not Cool'
    }

    hockey_set = (
        'Capitals',
        'Avalanche',
        'Blues',
        'Penguins'
    )

    print_dict(hockey_dict)
    print_set(hockey_set)
