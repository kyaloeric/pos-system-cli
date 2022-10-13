import os


def queries_options():
    print('***Products Queries***')

    # User option to chose from the options menu
    print("[1]. Search for a product")
    print("[2]. List all products")
    print("[3]. Search for product and their its history")
    print("[0]. Go Back to Main Menu")


def product_queries():
    queries_options()
    from product_operations.products import SearchProduct
    from product_operations.products import DisplayAllProducts
    choice = int(input("Enter your choice: "))

    while True:
        if choice == 1:
            SearchProduct()
        elif choice == 2:
            DisplayAllProducts()
        elif choice == 3:
            pass

        elif choice == 0:
            print("Exiting")
        else:
            print(" Oops!! Wrong choice!!")

        product_queries()


