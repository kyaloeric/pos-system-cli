# update customer
def update_customer():
    import sys
    import fileinput

    a = input("Enter customer name to be replaced:")
    b = input("Enter the new customer name")

    for n in fileinput.input(files="customers.txt"):
        n = n.replace(a, b)
        sys.stdout.write(n)
