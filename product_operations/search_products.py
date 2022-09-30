# search specific customer and or product


def search_products():
    with open("customers.txt", "r") as f:
        file_contents = f.read().splitlines()

    product_name = input("Please enter the name you want to find: ")

    for line, row in enumerate(file_contents):
        if product_name in row:
            print('Name "{0}" found in line {1}'.format(product_name, line))


# another approach
line = 0

names = open("customers.txt", "r")
name1 = names.readlines()

customer_name = input("Please enter the name you want to find: ")
for name in name1:
    # noinspection PyBroadException
    try:
        print(name)
        print(line)
        if name == customer_name:
            print(f"Found name: {name} \nLine No. {line + 1}")
        else:
            line = line + 1
    except:
        print("Unable to process")
