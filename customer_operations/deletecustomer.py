# code to delete a particular customer details
# data from a file
# open file in read mode


def delete_customer():
    with open("customers.txt", "r") as f:
        # read data line by line
        data = f.readlines()

    # open file in write mode
    with open("customers.txt", "w") as f:
        for line in data:

            # condition for data to be deleted by name
            name = str(input("Enter the customers Name:  "))
            if line.strip("\n") != name:
                f.write(line)
                print('The customer name"{0}" has been deleted'.format(name, line))


