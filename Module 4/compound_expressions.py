# Sean Gilbert
# CIS 189 Fall 2020
# program uses compound expression to test variable


if __name__ == '__main__':
    MAX = 10
    MIN = 0
    x = 10

    if MIN < x < MAX:
        print('var is between')
    elif MIN <= x < MAX:
        print('greater/equal to min, less than max')
    elif MIN < x <= MAX:
        print('more than min, equal/less than max')
