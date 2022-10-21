from customeroperations.customer_menu import *
from productoperations.product_menu import *
from purchaseoperations.purchases import *


def main_menu_operations():
    print("===WELCOME TO ROCKS STORE POS===")
    print("[1] Handle customers")
    print("[2] Handle products")
    print("[3] purchase operations")
    print("[0] Exit")


def main_menu():
    main_menu_operations()
    print()
    choice = int(input("Enter your option: "))
    while choice != 0:
        if choice == 1:
            print("You are dealing with customer operations")
            customer_main()
        elif choice == 2:
            print("You are dealing with product operations")
            product_main()
        elif choice == 3:
            print("You are dealing with purchase operations")
            purchases_menu()
        elif choice == 0:
            print("Exited successfully")
            quit()
        else:
            print(" Invalid option")

        print("Thanks for using the menu, Goodbye!!")
