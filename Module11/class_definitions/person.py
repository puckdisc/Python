class Person:
    """Person Class"""

    def __init__(self, lname, fname, addy=''):  # constructor
        name_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_chars.issuperset(lname) or not name_chars.issuperset(fname):
            raise ValueError('invalid name chars')
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return self.last_name + ", " + self.first_name + " lives at " + self.address


class Student(Person):
    """Student class"""
    def __init__(self, fname, lname, addy, major, start_date, gpa):
        super().__init__(lname, fname, addy)
        self.major = major
        self.start_date = start_date
        if not isinstance(gpa, (int, float)):
            raise ValueError('gpa not int or float')
        self.gpa = gpa

    def __repr__(self):
        return "lname={:}, fname={:}, addy={:}, major={:}, start_date={:}, gpa={:}".format(
            self.last_name, self.first_name, self.address, self.major, self.start_date, self.gpa)

    def __str__(self):
        return "{:}, {:}, {:}, {:}, {:}, {:}".format(
            self.last_name, self.first_name, self.address, self.major, self.start_date, self.gpa)

    def change_major(self, major):  # change major
        name_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_chars.issuperset(major):
            raise ValueError('invalid name chars')
        self.major = major

    def change_gpa(self, gpa):  # change gpa
        if not isinstance(gpa, (int, float)):
            raise ValueError('gpa not int or float')
        self.gpa = gpa

    def display(self):
        return "Student: {:} {:}\nMajor: {:}\nGPA: {:}".format(self.first_name, self.last_name,
                                                                   self.major, self.gpa)


# Driver
person123 = Person('Nathan', 'MacKinnon', 'Colorado')
student123 = Student('Nathan', 'MacKinnon', 'Colorado', 'Undecided', '10/1/20', 4.0)
student123.change_major('Being awesome')
# student123.change_major(123)
student123.change_gpa(3.0)
# student123.change_gpa('abc')
print(student123.display())
del student123
