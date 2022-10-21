# POS-CLI

### Introduction.

PO-CLI is a point of sale system that entirely works on the commandline whereby the user is prompted to
    make choices stepwise based on certain specific actions that leads towards the solution of what he intends to do. This has been achieved through the implementation of a python program that presents the user with a menu on where he picks the choices from, and they are processed.
#### Prerequisite.

  * python 3

### Features.

The entry point of the program is the main menu which presents the user with the main options to chose from depending on what he intends to do. The options entail Customer Operations, Product operations and Purchase operation  

## 1. Customer Operations
Customer_operations is the first choice at the main menu, under  it there is sub features whereby the User can Add customer, delete customer, update customer and also carry out query operations like viewing a single customer, or getting all the customers using either customer ID or customer name.The storage used for customers is the customers.txt file.  
## 2. Product Operations
Product operations is the second choice at the main menu, under it  there is sub features whereby the User can Add product, delete customer, update product and also carry out query operations like viewing a single product, or getting all the product using either customer ID or product name.The storage used for product is the products.txt file.
## 3. Purchase Operation
Purchasing operations is the third choice at the main menu, the user searches whether the product and the customer exists using either ID's or names before the purchasing process is initiated. If one is missing either the customer or the product, an error message is thrown and the purchasing process does not take place. If both exist, the next step is to check whether the available quantity of the product to be purchased is available, if it's not an error message is thrown prompting the user to enter a lower amount. When all the conditions are met then purchasing process is done. A customer can buy multiple items at the same time. A receipt is then generated upon checkout.The storage used for purchase is the purchases.txt file.    
### Setup and Run the project  


    1.Download the zipped files.

    2.Extract to your folder of choice.

    3.Open the extracted folder in a terminal of your choice.