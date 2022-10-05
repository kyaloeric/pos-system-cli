import os

from mainmenu.mainMenu import main_menu


def queries_options():
    print('***Products Queries***')

    # User option to chose from the options menu
    print("[1]. Search for a product")
    print("[2]. List all products")
    print("[3]. Search for product and their its history")
    print("[0]. Go Back to Main Menu")


def product_queries():
    from product_operations.search_products import search_products
    from mainmenu.mainMenu import main_menu
    from product_operations.displayproducts import prod_details
    from product_operations.addproduct import add_product
    queries_options()

    # take user choice
    choice = input("Please enter your choice to proceed: ")

    while True:
        # searches customer by name
        if choice == 1:
            search_products()
            main_menu()

        # choice 2 lists all the customers
        elif choice == 2:
            prod_details()
            main_menu()

        # search for a product  by ID and their purchase history
        elif choice == 3:
            product_id = (input('Enter product ID for the product you wish to search: '))

            with open("products.txt", "r") as f:
                file_stuff = f.read().splitlines()

                for line, row in enumerate(file_stuff):
                    if product_id in row:
                        print(
                            "The search result is" + 'product_id "{0}" found in line {0}'.format(product_id, line))

                        # purchase history
                        purchase_history = []
                        f = open('products.txt', 'r')
                        if os.stat('Files/products.txt').st_size == 0:
                            print('Purchase History for this product is Empty!')
                            main_menu()
                        else:
                            purchases = f.load(f)
                            for history in purchases:
                                if history.get("product_id") == product_id:
                                    purchase_history.append(history)

                            if len(purchase_history) == 0:
                                print('Purchase History for this Customer is Empty!')
                                main_menu()
                            else:
                                print('Purchase History for this Product is: ' + str(purchase_history))
                                main_menu()
                    else:
                        print('Cant find a product with this search ID!')
                        main_menu()
        # choice 0 takes us back to main menu
        elif choice == 0:
            main_menu()

        # Invalid choice takes us back to main menu
        else:
            print('Warning! Wrong choice.')
            main_menu()
