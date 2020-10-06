def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """prompt for test name and test score then prints the inputs

    The test name string must not be empty. The test score must be between
    0 and 100. If both inputs are valid, they are printed.

    :param test_name: string name of test
    :param test_score: integer test score
    :param invalid_message: string error message
    :return: pass
    """
    while True:
        if 0 <= test_score <= 100:
            print(test_name, test_score)
            # return {test_name: test_score}
            return True
        else:
            print(invalid_message)
            return False


if __name__ == '__main__':

    test_name = input('Enter test name: ')
    test_score = input('Enter test score: ')
    try:
        test_score = int(test_score)
        score_input(test_name, test_score)

    except ValueError:
        print('Score must be an integer. Try again')




