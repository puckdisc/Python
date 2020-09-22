# Sean Gilbert
# CIS 189 Fall 2020
# Last Modified 09/21/20



def average(score1, score2, score3):
    NUMBER_TESTS = 3

    if score3 < 0:
            raise ValueError

    return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    average()
