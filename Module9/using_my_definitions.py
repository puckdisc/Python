import my_definitions as md

# imports and uses module

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
    md.author('Bob')
    md.print_dict(hockey_dict)
    md.print_set(hockey_set)
