from definitions import greeting
from definitions import dictionary_ops
from definitions import set_ops


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

    greeting.friendly_greeting()
    greeting.print_author('Ovi')
    dictionary_ops.print_dictionary(hockey_dict)
    set_ops.print_set(hockey_set)
