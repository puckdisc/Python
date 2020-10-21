import my_definitions as md


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

    md.greeting()
    md.author()
    md.print_dict(hockey_dict)
    md.print_set(hockey_set)
