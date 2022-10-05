class CustomerOperations:
    def __init__(self, phone_number, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    # add a new customer
    @classmethod
    def add_customer(cls):
        foo = open("customers.txt", "a+")
        name = input("Enter name: ")
        age = input("Enter customer age: ")
        phone_number = int(input("enter the number: "))
        foo.write(str(age) + "\n " + name + " \n" + str(phone_number) + "\n")  # new line
        print('Customer added successfully.')
        foo.close()

    # delete customer by name
    @classmethod
    def delete_customer(cls, name):
        with open("customers.txt", "r") as f:
            # read data line by line
            data = f.readlines()

        # open file in write mode
        with open("customers.txt", "w") as f:
            for line in data:

                # condition for data to be deleted by name
                name = str(input("Enter the customers Name:  "))
                if line.strip("\n") != name:
                    f.write(line)
                    print('The customer name"{0}" has been deleted'.format(name, line))

    # update customer by name
    @classmethod
    def update_customer(cls):
        import sys
        import fileinput

        a = input("Enter customer name to be replaced:")
        b = input("Enter the new customer name")

        for n in fileinput.input(files="customers.txt"):
            n = n.replace(a, b)
            sys.stdout.write(n)


def read():
    return None
