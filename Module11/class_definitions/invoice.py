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
        return "{:}, {:}, {:}, {:}, {:}".format(self.customer_id, self.last_name,
                                                self.first_name, self.phone_number, self.address)

    def __repr__(self):
        return "customer_id:{:}, last_name:{:}, first_name:{:}, phone_number:{:}, " \
               "address:{:}".format(self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def display(self):
        # print string representation of object
        print(self)


class Invoice(Customer):

    """
    Class Invoice
    Required: invoice_id, customer_id, last_name, first_name, phone_number, address
    Optional: items_with_price
    """

    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address):
        # constructor
        self.invoice_id = invoice_id
        super().__init__(customer_id, last_name, first_name, phone_number, address)
        name_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not name_chars.issuperset(first_name) or not name_chars.issuperset(last_name):
            raise ValueError('invalid name char')
        self.items_with_price = {}

    def __str__(self):
        return 'Invoice: %s, %s, %s, %s, %s, %s'\
               % (self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def __repr__(self):
        return 'Invoice: invoice_id=%s, customer_id=%s, last_name=%s, first_name=%s, phone_number=%s, address=%s'\
               % (self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def add_item(self, item):  # add to items_with_price dict
        self.items_with_price.update(item)

    def create_invoice(self):  # function creates and prints invoice based from class attributes

        # initialize local variable subtotal
        subtotal = 0

        # print invoice header
        print("Customer #{:}: {:}, {:}".format(self.customer_id, self.last_name, self.first_name))
        print("Phone: {:}".format(self.phone_number))
        print("Address: {:}".format(self.address))
        print("----------------")


        # iterate through dictionary, print each pair, add price to subtotal, calculate tax/totals
        for key, value in self.items_with_price.items():
            subtotal += value
            print("{:}...${:.2f}".format(key, value))
        tax = (subtotal * 0.06)
        total = subtotal + tax

        # print invoice totals
        print("----------------")
        print("Subtotal...${:.2f}".format(subtotal))
        print("Tax...${:.2f}".format(tax))
        print("Total...${:.2f}".format(total))


# Driver

captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice3 = Invoice(1, 1, 'Reynolds', 'Mel', 'No phones', "Firefly, somewhere in the verse")
invoice3.add_item({'iPad': 799.99})
invoice3.add_item({'Surface': 999.99})
invoice3.add_item({'Lenovo': 819.99})
invoice3.add_item({'Warranty': 100.00})
invoice3.create_invoice()
