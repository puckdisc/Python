def write_to_file(fun_tuple_to_add):
    """
    Appends passed parameter to txt file.

    :param fun_tuple_to_add: tuple parameter
    :return: none. writes tuple to file then closes.
    """
    f = open('student_info.txt', 'a')
    # for tup in fun_tuple_to_add:
    f.write(str(fun_tuple_to_add) + '\n')
    f.close()


def get_student_info(**kwargs):
    """
    Asks for test scores of students and combines into tuples.

    Program declares lists for kwarg and score values. Asks for score entries until user
    inputs 999. Scores are combined into a single list tuple with associated keyword values and
    list is converted to tuple and returned.

    :param kwargs: keywords attached to test score.
    :return: returns tuple of keywords and associated test scores
    """
    #Declares lists and tuple
    score_list = []
    kwarg_list = []
    student_score_tuple = ()

    # Ask for scores until 999 is entered then combines into list
    while True:
        try:
            test_score = int(input('Enter a test score to add to file. Enter 999 to stop: '))
        except ValueError:
            test_score = 0
        if test_score == 999:
            break
        score_list.append(test_score)

    for key, value in kwargs.items():
        kwarg_list.append(value)

    tuple_list = kwarg_list + score_list
    tuple(tuple_list)
    student_score_tuple = student_score_tuple + (tuple_list, )

    write_to_file(student_score_tuple)


def read_from_file():
    """

    :return:
    """

    f = open('student_info.txt', 'r')
    for line in f:
        print(line)
    f.close()


if __name__ == '__main__':

    while True:
        any_key = input('Press any key to end: ')
        if any_key is not '':
            print('Program ending.')
            break
        print('Nothing entered. Program is proceeding...')

        get_student_info(first_name='bob', last_name='williams')
        get_student_info(first_name='marsha', last_name='jones')
        get_student_info(first_name='sadiq', last_name='washington')
        get_student_info(first_name='kathy', last_name='griffin')

        read_from_file()
        break
