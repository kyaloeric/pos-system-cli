# customer menu options
from customeroperations.customers import add_customer, update_customer, delete_customer


def customerMenu():
    print()
    print("   CUSTOMER MENU ")
    print(" --- Make a choice to continue---")
    print()
    print("[1] Add customer.")
    print("[2] Update customer.")
    print("[3] Delete customer.")
    print("[4] Customer queries")
    print("[0] Exit to the main menu.")


def customer_main():
    from mainmenu.main_menu import main_menu
    from customeroperations.customer_queries import customer_queries
    customerMenu()
    print()
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
