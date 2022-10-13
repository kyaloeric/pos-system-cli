import random


def search_product():
    lt = []
    with open("products.txt", "r") as z:
        pid = int(input("Enter Product Id: "))
        for Line in z:
            if str(pid) in Line:
                lt.append(Line)
                print(lt)


def make_purchase():
    transaction_list = []
    purchase_dictionary = {}
    shopping_cart = []
    list_quantity = []
    list_price = []
    prod = []
    customer_id = input("Enter the Customer's Id: ")

    loop1 = 1

    while loop1 == 1:
        add_item = input('Add product to purchase? Y/N?: ').upper()
        if add_item == 'Y':
            product_id = input("Enter Product Id: ")
            quantity = int(input("Quantity: "))
            list_quantity.append(quantity)  # adding quantity to the declared empty list
            purchase_id = random.randint(2000, 2000000)
            with open("products.txt", "r") as f:
                fprodlist = f.readlines()
                for Line in fprodlist:
                    if product_id in Line:
                        line_index = fprodlist.index(Line)
                        product = Line.split(',')
                        product_name = product[1]
                        product_quantity = product[3]
                        price = product[4]

            with open("customers.txt", "r") as t:
                clist = t.readlines()
                for Line1 in clist:
                    if customer_id in Line1:
                        cust = Line1.split(',')
                        customer_name = cust[1]

            # adding product name to the declared empty list

            shopping_cart.append(product_name)
            new_quantity = (int(product_quantity) - quantity)
            total_price = (int(price) * quantity)

            # adding the total price of product times quantity to the declared empty list
            list_price.append(total_price)
            prod[3] = str(new_quantity)
            s = ','
            fprodlist[line_index] = s.join(prod)

            total = 0
            for i in range(0, len(list_price)):
                total = total + list_price[i]
            purchase_dictionary['Purchase ID'] = purchase_id
            purchase_dictionary['Customer Name'] = customer_name
            purchase_dictionary['Products Name'] = shopping_cart
            purchase_dictionary['Products Quantity'] = list_quantity
            purchase_dictionary['Cumulative Product Prices'] = list_price
            purchase_dictionary['Total'] = total
            transaction_list.append(purchase_dictionary)
            with open('products.txt', 'w') as outfile:
                for Line in fprodlist:
                    outfile.write(Line)
        elif add_item == 'N':
            with open('purchases.txt', 'a') as outfile1:
                outfile1.write('\n')
                outfile1.write(str(transaction_list))
            print("The Purchase is Successful!...")
            for key, value in purchase_dictionary.items():
                print(key, value)
            purchases_menu()


def purchases_menu():
    print("[1]. Search a Product")
    print("[2]. Purchase product")
    print("[3]. Main Menu")
    print("[0]. Exit")

    choice = int(input("choose one option: "))
    while choice:
        if choice == 1:
            search_product()
        elif choice == 2:
            make_purchase()
        elif choice == 3:
            from mainmenu.mainMenu import main_menu
            main_menu()
        elif choice == 0:
            print()
            print('The System  is Exiting! Goodbye...')
        else:
            print("Oops, Wrong Choice!")
