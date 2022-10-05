def add_product():
    foo = open("products.txt", "a+")
    product_id = input("Enter product ID: ")
    with open("products.txt", 'r') as f:

        for line in f.readlines():
            prod_list = []
            line_data = line.split(',')
            prod_list.append(line_data[0])

            if product_id in prod_list:
                print("Oops!! product id exists! enter another ID")
                return add_product()
    product_quantity = input("Enter the quantity for the product: ")
    product_name = input("Enter the product name: ")
    serial_number = (input("Enter the serial number: "))
    foo.write(product_id + " " + product_quantity + " " + product_name + " " + str(serial_number))  # new line
    print("product added successfully")
    foo.close()
    output = {"id": product_id, "quantity": product_quantity, "name": product_name, "Serial Number": serial_number}
    return output


