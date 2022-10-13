import os

from mainmenu.mainMenu import main_menu


def queries_options():
    print('***Customers Queries***')

    # user options to choose from to perform more customer queries
    print("[1]. Search for a customer")
    print("[2]. List all customers")
    print("[3]. Search for customer by ID and their purchase history")
    print("[0]. Go Back to Main Menu")


def customer_queries():
    queries_options()

    from customer_operations.customers import SearchCustomer
    from customer_operations.customers import DisplayAllCustomers
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            SearchCustomer()
        elif choice == 2:
            DisplayAllCustomers()
        elif choice == 3:
            pass
        elif choice == 0:
            main_menu()
            print("Exiting")
        else:
            print(" Oops!! Wrong choice!!")

        customer_queries()
