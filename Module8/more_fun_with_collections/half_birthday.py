import datetime
from dateutil.relativedelta import relativedelta


def half_birthday(birthday):
    half_birthday = birthday + relativedelta(months=+6)
    return half_birthday



if __name__ == '__main__':
    birthday = datetime.datetime(2015, 5, 10)
    half_birthday(birthday)
