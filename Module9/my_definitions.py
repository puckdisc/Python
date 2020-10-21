def greeting():
    print('Greetings, friend!')


def author():
    print('I am the author of this code')


def print_dict(fun_dict):
    for key, value in fun_dict.items():
        print(key, 'are', value)


def print_set(fun_set):
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
