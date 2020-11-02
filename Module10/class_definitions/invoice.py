class Invoice:

    """
    Class Invoice

    Required: invoice_id, customer_id, last_name, first_name, phone_number, address
    Optional: items_with_price


    """

    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address):
        # constructor
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
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
        print("Invoice: {:}, Customer: {:} {:}".format(self.invoice_id, self.first_name, self.last_name))
        print("----------------")

        # iterate through dictionary, print each pair, add price to subtotal, calculate tax/totals
        for key, value in self.items_with_price.items():
            subtotal += value
            print("{:}...${:}".format(key, value))
        tax = (subtotal * 0.06)
        total = subtotal + tax

        # print invoice totals
        print("----------------")
        print("Subtotal...${:.2f}".format(subtotal))
        print("Tax...${:.2f}".format(tax))
        print("Total...${:.2f}".format(total))


# Driver
invoice = Invoice(1, 123, 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr, Anaheim, CA 92802')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
