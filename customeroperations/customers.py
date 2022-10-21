import random


class CustomerOperations:
    def __init__(self, customer_id, phone_number, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    # add a new customer


def add_customer():
    customer_id = random.randint(10000, 100000)
    customer_name = input("Enter the name of the customer: ")
    customer_phone = input("Enter the phone number of the customer: ")
    customer_email = input(" Enter the email address")

    z = f'{customer_id},{customer_name},{customer_phone},{customer_email}\n'

    with open('customers.txt', 'a') as outfile:
        print("A new Customer has been Added successfully.")
        outfile.write(z)


# delete customer by ID
def delete_customer():
    with open("customers.txt", "r") as f:
        f_list = f.readlines()
        customer_id = input("Enter the customer's ID: ")
        for Line in f_list:
            if customer_id in Line:
                line_index = f_list.index(Line)

                f_list.pop(line_index)

        with open('customers.txt', 'w') as outfile:
            print("The Customer has been  Deleted successfully.")
            for Line in f_list:
                outfile.write(Line)


# update customer by name
def update_customer():
    with open("customers.txt", "r") as f:
        f_list = f.readlines()
        customer_id = input("Enter the customer ID: ")
        for Line in f_list:
            if customer_id in Line:
                line_index = f_list.index(Line)

                new_number = input("Enter the new phone number : ")
                new_name = input(" Enter the new name: ")
                k = Line.split(',')
                k[1] = new_name
                x = Line.split(',')
                x[2] = new_number
        f = ','
        f_list[line_index] = f.join(x)

        with open('customers.txt', 'w') as outfile:
            print("Customer Updated successfully.")
            for Line in f_list:
                outfile.write(Line)


# search customer by ID
def search_customer():
    found_cust = []
    with open("customers.txt", "r") as f:
        customer_id = int(input("Please enter Customer's ID: "))
        for Line in f:
            if str(customer_id) in Line:
                found_cust.append(Line)
                print(found_cust)
            else:
                print("The customer with this ID does not exist")


# search customer by name

def search_customer_by_name():
    found_cust = []
    with open("customers.txt", "r") as f:
        customer_name = input("Please enter Customer's Name: ")
        for Line in f:
            if str(customer_name) in Line:
                found_cust.append(Line)
                print(found_cust)
            else:
                print("The customer with this name does not exist")


# fetch all the customers by displaying their details
def display_all_customers():
    all_customers = []
    with open("customers.txt", "r") as f:
        all_cust = f.readlines()
        for Lines in all_cust:
            all_customers.append(Lines)
        print(all_customers)


# search customer and display their purchase history
def display_customers_purchase_history():
    purchase_history = []
    with open("purchases.txt", "r") as f:
        customer_name = input(" Enter the customers ID: ")
        for line in f:
            if str(customer_name) in line:
                purchase_history.append(line)
                print(purchase_history)

            else:
                print("Purchase history for that customer is empty")
