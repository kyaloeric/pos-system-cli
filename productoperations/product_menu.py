# product menu options

def product_menu():
    print(" PRODUCTS MENU")
    print("--Make a choice to continue--")
    print("[1] Add product.")
    print("[2] Update product.")
    print("[3] Delete product.")
    print("[4] Product queries")
    print("[0] Exit to the main menu.")


def product_main():
    from mainmenu.main_menu import main_menu
    from productoperations.products import add_product, delete_product, update_product
    from productoperations.product_queries import product_queries

    product_menu()
    print()
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
