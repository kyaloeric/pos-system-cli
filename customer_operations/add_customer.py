# customer_details = []


def add_customer():
    foo = open("customers.txt", "a+")
    name = input("Enter name: ")
    age = input("Enter customer age: ")
    phone_number = int(input("enter the number: "))
    foo.write(str(age) + "\n " + name + " \n" + str(phone_number) + "\n")  # new line
    print('Customer added successfully.')
    foo.close()


