# customer menu options
from customer_operations.customers import add_customer, update_customer, delete_customer


def customerMenu():
    print(" KINDLY MAKE A CHOICE TO CONTINUE")
    print("[1] Add customer.")
    print("[2] Update customer.")
    print("[3] Delete customer.")
    print("[4] Customer queries")
    print("[0] Exit to the main menu.")


def customer_main():
    from mainmenu.mainMenu import main_menu
    from customer_operations.customerQueries import customer_queries
    customerMenu()
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            print(" A customer is going to be inserted")
            add_customer()
        elif choice == 2:
            print("A customer is going to be updated")
            update_customer()
        elif choice == 3:
            print("A customer is going to be deleted")
            delete_customer()
        elif choice == 4:
            print(" customer queries")
            customer_queries()

        elif choice == 0:
            print("Exiting")
            main_menu()
        else:
            print(" Oops!! Wrong choice!!")

        customer_main()
