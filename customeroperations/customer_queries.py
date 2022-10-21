import os

from mainmenu.main_menu import main_menu


def queries_options():
    print('***Customers Queries***')

    # user options to choose from to perform more customer queries
    print("[1]. Search for a customer")
    print("[2]. List all customers")
    print("[3]. Search for customer by ID and their purchase history")
    print("[0]. Go Back to Main Menu")


def customer_queries():
    queries_options()
    print()
    from customeroperations.customers import search_customer
    from customeroperations.customers import display_all_customers
    from customeroperations.customers import display_customers_purchase_history
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            search_customer()
        elif choice == 2:
            display_all_customers()
        elif choice == 3:
            display_customers_purchase_history()
        elif choice == 0:
            main_menu()
            print("Exiting")
        else:
            print(" Oops!! Wrong choice!!")

        customer_queries()
