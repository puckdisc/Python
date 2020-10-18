def get_test_scores():
    """
    Creates dictionary of test scores

    Asks for the number of scores to be entered. Adds a key/value pair for each score.
    Returns a dictionary of the score1, score2, score3, and associated values

    :return: dictionary of scores
    """
    scores_dict = dict()

    while True:
        try:
            # request number of scores to be entered
            num_scores = int(input('Enter the number of test scores: '))
        except ValueError:
            # non integer input. try again
            print('You must enter an integer. Try again. ')
            continue
        else:
            # valid input. continuing
            break

    for s in range(num_scores):
        # creates key for pair
        score_key = 'score' + str(s+1)
        while True:
            try:
                # get score value
                score_value = int(input('Enter the integer test score: '))
            except ValueError:
                print('You must enter an integer. Try again. ')
                continue
            else:
                # combines key and value. updates dictionary accordingly
                score = {score_key: score_value}
                scores_dict.update(score)
                break
    return scores_dict


def average_scores(scores_dict):
    """
    Calculates value average in score dictionary

    Iterates through score dictionary by generating the predicted key and pulling the value.
    Value is added to a sum then divided by len(dictionary) to get average. Float avg is returned.

    :param scores_dict: score dictionary from get_test_scores().
    :return:
    """
    score_sum = 0
    for s in range(len(scores_dict)):
        # generate key and pull associated value then average scores
        score_key = 'score' + str(s+1)
        score_value = scores_dict[score_key]
        score_sum = score_sum + score_value
    avg = score_sum/len(scores_dict)

    return avg


if __name__ == '__main__':
    average_scores(get_test_scores())
