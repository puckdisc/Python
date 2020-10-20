def switch_average(letter):
    """
    Accepts letter and returns minimum score

    Accepts str letter key and uses .get() to search dictionary for key

    :param letter: string input key
    :return: integer value
    """

    min_score = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 0
    }

    switch = min_score.get(letter, lambda: 'Invalid Entry')
    return switch


if __name__ == '__main__':
    switch_average('H')

