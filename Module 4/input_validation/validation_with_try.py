# Sean Gilbert
# CIS 189 Fall 2020
# Last Modified 09/21/20


def average(score1, score2, score3):
    NUMBER_TESTS = 3

    try:
        negative_test = score1*score2*score3
    finally:
        if negative_test >= 0:
            return float((score1 + score2 + score3)/NUMBER_TESTS)
        elif negative_test < 0:
            raise ValueError


if __name__ == '__main__':
    average()
