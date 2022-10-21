def beautiful_printer(purchase_dictionary, titles, width):
    formatting = ""
    for number in width:
        formatting += "{:<" + str(number) + "}"
    print(formatting.format(*titles))
    for key, value in purchase_dictionary.iteritems():
        sv = []
        for subvalue in value:
            sv.append(subvalue)
        print(formatting.format(key, *sv))
