# code to delete a particular customer details
# data from a file
# open file in read mode


def delete_product():
    with open("products.txt", "r") as f:
        # read data line by line
        data = f.readlines()

    # open file in write mode
    with open("products.txt", "w") as f:
        for line in data:

            # condition for data to be deleted by name
            prod_name = str(input("Enter the product's Name:  "))
            if line.strip("\n") != prod_name:
                f.write(line)
                print('The product prod_name"{0}" has been deleted successfully'.format(prod_name, line))


