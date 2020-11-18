class Customer:
    """
    Class Customer comprised of customer_id, last_name, first_name, phone_number, address.

    All 5 attributes are required.
    AttributeError is raised on non-numeric customer_id.
    Four remaining attributes are string.
    """

    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        self.customer_id = customer_id
        if isinstance(self.customer_id, int) is True:
            self.customer_id = int(customer_id)
        else:
            raise AttributeError("'Customer object' has no attribute 'customer_id'")
        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.phone_number = str(phone_number)
        self.address = str(address)

    def __str__(self):
        return str(self.customer_id) + self.last_name + self.first_name

    def __repr__(self):
        return 'in repr' + '\n' + str(self.customer_id) + '\n' + str(self.first_name) + ' ' + str(self.last_name)

    def display(self):
        # print string representation of object
        print(self)


# Driver
customer1 = Customer(1234, 'Bharara', 'Preet', '202-456-7890', '1600 Pennsylvania Avenue')
customer1.display()       # display returns a str, so print the information
del customer1

#customer2 = Customer('abc', 'Bharara', 'Preet', '202-456-7890', '1600 Pennsylvania Avenue')
#customer2.display()
#del customer2
