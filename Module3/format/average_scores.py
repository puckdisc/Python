# Sean Gilbert
# Last Modified 09/13/20
# collects inputs, calculates average, outputs name and scores

def average():
    score1 = int(input("Enter the first score: "))
    score2 = int(input("Enter the second score: "))
    score3 = int(input("Enter the third score: "))
    avg = (score1+score2+score3)/3

    return round(avg, 2)


if __name__ == '__main__':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))

    average_scores = average()

    print(last_name + ',', first_name, ' Age:', age, ' Grade:', average_scores)
