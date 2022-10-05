# customer_details = []


def add_customer():
    foo = open("customers.txt", "a+")
    customer_id = 1
    name = input("Enter customer name: ")
    age = input("Enter customer age: ")
    phone_number = int(input("enter the number: "))
    foo.write(str( customer_id) + " " + str(age) + " " + name + " " + str(phone_number) + " ")  # new line
    print('Customer added successfully.')
    foo.close()


