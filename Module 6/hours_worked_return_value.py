def hourly_employee_input():
    """asks for name, hours worked, wage, then combines and outputs"""
    name = input('Please enter your name: ')
    hours_worked = int(input('Please enter the number of hours worked: '))
    hourly_pay_rate = float(input('Please enter your wage: '))
    pay = weekly_pay(hours_worked, hourly_pay_rate)

    return name + " earned $" + str(pay) + " net pay."


def weekly_pay(hours_worked, hourly_pay_rate):
    """accepts hours_worked and hourly_pay_rate returns product"""
    return hours_worked*hourly_pay_rate


if __name__ == '__main__':
    try:  # check for ValueError
        print(hourly_employee_input())
    except ValueError as err:
        print('Value Error encountered. Verify proper inputs')
