def hourly_employee_input():
    """asks for name, hours worked, wage, then combines and outputs"""
    name = input('Please enter your name: ')
    hours = int(input('Pleas enter the number of hours worked: '))
    wage = float(input('Please enter your wage: '))

    print(name, hours, wage)


if __name__ == '__main__':
    try:  # check for ValueError
        hourly_employee_input()
    except ValueError as err:
        print('Value Error encountered. Verify proper inputs')
