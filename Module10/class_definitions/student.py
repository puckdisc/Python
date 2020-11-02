class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not name_characters.issuperset(lname) and name_characters.issuperset(fname):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return "Student: %s, %s, %s, %s" % (self.last_name, self.first_name, self.major, self.gpa)

    def __repr__(self):
        return "Student: lname=%s, fname=%s, major=%s, gpa=%s" % (self.last_name, self.first_name, self.major, self.gpa)

    def display(self):
        return self.first_name + ' ' + self.last_name + " is majoring in " + self.major +\
                                     " with GPA: " + str(self.gpa)

# Driver
student = Student('Ovechkin', 'Alex', 'Goal Scoring', 4.0)
print(str(student))
