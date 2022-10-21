import random
from mainmenu.main_menu import main_menu


class ProductOperations:
    def __init__(self, product_id, product_name, product_quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.price = price

    # add new product


def add_product():
    product_id = random.randint(100, 10000)
    product_name = input("Enter the name of the product: ")
    product_type = input("Enter the type of product: ")
    product_quantity = int(input("Enter the quantity/amount of the product: "))
    price = int(input("Enter the price of the product: "))
    z = f'{product_id},{product_name},{product_type},{product_quantity},{price}\n'

    with open('products.txt', 'a') as outfile:
        print('Product has been added successfully added')
        outfile.write(z)


def update_product():
    with open("products.txt", "r+") as f:
        f_list = f.readlines()
        cid = input("Enter the product ID: ")
        for Line in f_list:
            if cid in Line:
                line_index = f_list.index(Line)
                user_input = input("Enter the New product Quantity: ")
                new_price = input("Enter the New Price: ")
                k = Line.split(',')
                k[3] = user_input
                k[4] = new_price
        f = ','
        f_list[line_index] = f.join(k)

        with open('products.txt', 'w') as outfile:
            print('Product has been updated successfully')
            for Line in f_list:
                outfile.write(Line)


def delete_product():
    with open("products.txt", "r") as s:
        p_list = s.readlines()
        product_id = input("Enter the product ID: ")
        for Line in p_list:
            if product_id in Line:
                line_index = p_list.index(Line)
                p_list.pop(line_index)
        with open('products.txt', 'w') as outfile:
            print('Product has been successfully deleted')
            for Line in p_list:
                outfile.write(Line)


# search product by ID
def SearchProduct():
    found_product = []
    with open("products.txt", "r") as f:
        product_id = int(input("Please enter Product's ID: "))
        for Line in f:
            if str(product_id) in Line:
                found_product.append(Line)
                print(found_product)
            else:
                print("The product with this ID does not exist")


# search customer by name

def SearchCustomerByName():
    found_cust = []
    with open("products.txt", "r") as f:
        product_name = int(input("Please enter Customer's Name: "))
        for Line in f:
            if str(product_name) in Line:
                found_cust.append(Line)
                print(found_cust)
            else:
                # print("The product with this name does not exist")
                main_menu()


# display all the products
def DisplayAllProducts():
    all_products = []
    with open("products.txt", "r") as f:
        all_cust = f.readlines()
        for Lines in all_cust:
            all_products.append(Lines)
        print(all_products)
