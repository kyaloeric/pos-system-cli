# search specific customer and or product


def search_products():
    with open("customers.txt", "r") as f:
        file_contents = f.read().splitlines()

    product_name = input("Please enter the name you want to find: ")

    for line, row in enumerate(file_contents):
        if product_name in row:
            print('Name "{0}" found in line {0}'.format(product_name, line))


# another approach



