# small function to  display all customer details


def customer_details():
    details = open("customers.txt")
    for customer in details:
        name, age, phone_number = customer.split()
        print(name, age, phone_number)
    details.close()


