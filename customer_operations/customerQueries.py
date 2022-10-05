import os

from mainmenu.mainMenu import main_menu


def queries_options():
    print('***Customers Queries***')

    # user options to choose from to perform more customer queries
    print("[1]. Search for a customer")
    print("[2]. List all customers")
    print("[3]. Search for customer and their purchase history")
    print("[0]. Go Back to Main Menu")


def customer_queries():
    from customer_operations.search_customer import search_customer
    from mainmenu.mainMenu import main_menu
    from customer_operations.displaycustomer import customer_details
    queries_options()

    # take user choice
    choice = input('Please enter your choice to proceed: ')

    while True:
        # searches for a customer by name
        if choice == 1:
            search_customer()
            main_menu()

        # choice 2 lists all the customers
        elif choice == 2:
            customer_details()
            main_menu()

        # search for a customer by number and their purchase history
        elif choice == 3:
            phone_number = (input('Enter customer number for the customer you wish to search history: '))

            with open("customers.txt", "r") as f:
                file_contents = f.read().splitlines()

                for line, row in enumerate(file_contents):
                    if phone_number in row:
                        print("The search result is" + 'Phone_number "{0}" found in line {0}'.format(phone_number, line))

                        # purchase history
                        purchase_history = []
                        f = open('customers.txt', 'r')
                        if os.stat('Files/customers.txt').st_size == 0:
                            print('Purchase History for this Customer is Empty!')
                            main_menu()
                        else:
                            purchases = f.load(f)
                            for history in purchases:
                                if history.get("phone_number") == phone_number:
                                    purchase_history.append(history)

                            if len(purchase_history) == 0:
                                print('Purchase History for this Customer is Empty!')
                                main_menu()
                            else:
                                print('Purchase History for this Customer is: ' + str(purchase_history))
                                main_menu()
                    else:
                        print('Cant find a customer with this search ID!')
                        main_menu()
        # 0 takes us back to main menu
        elif choice == 0:
            main_menu()

        # This choice will take us back to main menu
        else:
            print('Oops!! Wrong choice.')
            main_menu()
