# update customer
def update_product():
    import sys
    import fileinput

    a = input("Enter name of existing product to be replaced: ")
    b = input("Enter the name of the new product  text: ")

    for n in fileinput.input(files="products.txt"):
        n = n.replace(a, b)
        sys.stdout.write(n)
