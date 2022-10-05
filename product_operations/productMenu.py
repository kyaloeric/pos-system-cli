# product menu options
from product_operations.addproduct import add_product
from product_operations.deleteproduct import delete_product
from product_operations.update_product import update_product


def productMenu():
    print(" KINDLY MAKE A CHOICE TO CONTINUE")
    print("[1] Add product.")
    print("[2] Update product.")
    print("[3] Delete product.")
    print("[4] Product queries")
    print("[0] Exit to the main menu.")


def product_main():
    from mainmenu.mainMenu import main_menu
    from product_operations.productQueries import product_queries
    productMenu()
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            print("A product is going to be added")
            add_product()
        elif choice == 2:
            print("A product is going to be updated")
            update_product()
        elif choice == 3:
            print("A product is going to be deleted")
            delete_product()
        elif choice == 4:
            print(" product queries")
            product_queries()

        elif choice == 0:
            print("Exiting")
            main_menu()

        else:
            print(" Oops!! Wrong choice!!")

        product_main()
