# search customer by name
def search_customer():
    with open("customers.txt", "r") as f:
        file_contents = f.read().splitlines()

    uname = input("Please enter the name you want to find: ")

    for line, row in enumerate(file_contents):
        if uname in row:
            print('Name "{0}" found in line {1}'.format(uname, line))
