# small function to  display product details


def prod_details():
    details = open("products.txt")
    for product in details:
        prod_name, mfg_date, serial_number = product.split()
        print(prod_name, mfg_date, serial_number)
    details.close()


