class Employee:

    """
    Class Employee.
    """
# Employee Class
    # Constructor
    def __init__(self, lname, fname, address, phone_number):
        name_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_chars.issuperset(lname) or not name_chars.issuperset(fname):
            raise ValueError('invalid name characters')
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = phone_number

    def __repr__(self):
        return "Employee: lname=%s, fname=%s, address=%s, phone_number=%s" \
                % (self._last_name, self._first_name, self._address,
                   self._phone_number)

    def __str__(self):
        return "%s, %s, %s, %s" \
               % (self._last_name, self._first_name, self._address,
                  self._phone_number)

    def display(self):
        print("{:} {:}\n{:}\n"
              .format(self._first_name, self._last_name, self._address))

class SalariedEmployee(Employee):
    """class Salaried employee based on Employee"""

    def __init__(self, lname, fname, start_date, salary):
        super(SalariedEmployee, self).__init__(lname, fname, address='', phone_number='')
        if not isinstance(salary, (int, float)):
            raise ValueError('salary not int or float')
        self._start_date = start_date
        self._salary = salary

    def give_raise(self, raise_amount):
        self._salary += raise_amount

    def display(self):
        return "Salaried Employee: {:} {:}\nStart Date: {:}\nSalary: ${:.2f}\n".format(
            self._first_name, self._last_name, self._start_date, self._salary)

class HourlyEmployee(Employee):
    def __init__(self, lname, fname, start_date, hourly_pay):
        super(HourlyEmployee, self).__init__(lname, fname, address='', phone_number='')
        if not isinstance(hourly_pay, (int, float)):
            raise ValueError('hourly pay not int or float')
        self._start_date = start_date
        self._hourly_pay = hourly_pay

    def give_raise(self, raise_amount):
        self._hourly_pay += raise_amount

    def display(self):
        return "Hourly Employee: {:} {:}\nStart Date: {:}\nWage: ${:.2f}/hour\n".format(
            self._first_name, self._last_name, self._start_date, self._hourly_pay)


# Driver
entry_level_salaried = SalariedEmployee('Patel', 'Sasha', '10/1/20', 40000)   # call the constructor, needs to have a first and last name in parameter
entry_level_hourly = HourlyEmployee('Patel', 'Sasha', '10/1/20', 10)
print(entry_level_salaried.display())
print(entry_level_hourly.display())

entry_level_salaried.give_raise(5000)  # give raises
entry_level_hourly.give_raise(2)

print(entry_level_salaried.display())  # display
print(entry_level_hourly.display())

del entry_level_salaried  # clean up
del entry_level_hourly
