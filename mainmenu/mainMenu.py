from customer_operations.customer_menu import customer_main
from product_operations.productMenu import product_main


def main_menu():
    print("***WELCOME TO ROCKS POS** ")
    print("[1] Handle customers")
    print("[2] Handle products")
    print("[3] Handle queries")
    print("[0] Exit")


def main():
    main_menu()
    choice = int(input("Enter your option: "))
    while choice != 0:
        if choice == 1:
            print("You are dealing with customer operations")
            customer_main()
        elif choice == 2:
            print("You are dealing with product operations")
            product_main()
        elif choice == 0:
            print("Exited successfully")
        else:
            print(" Invalid option")

        choice = int(input("Enter your option: "))

        main_menu()

        print("Thanks for using the menu, Goodbye!!")


if __name__ == '__main__':
    main()
