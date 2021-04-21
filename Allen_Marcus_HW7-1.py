#Author: Marcus Allen
#Assignment Number: 5
#Date: 4/12/2021
#Description: program that keeps track of a firm's inventory and prices

# function to input the inventory file into 2 dictionaries
def read_file(file_name, prices, quantities):
    infile = open(file_name, 'r')
    for line in infile:
        line = line.rstrip('\n')
        line_list = line.split(';')
        product = line_list[0]
        price = line_list[1]
        quantity = line_list[2]
        prices[product] = price
        quantities[product] = quantity
    infile.close()


# function that prints the option menu
def print_menu():
    print("""
Please select an option from the menu below:
1. View list of available products.
2. View details for one product.
3. Add a new product.
4. Update information for a product.
5. Exit.
""") 
    
#function that lets the user choose from the option menu
def get_user_choice():
    while True:
        try:
            print_menu()
            choice = int(input("What would you like to do?"))
            if choice > 5 or choice < 1:
                raise Exception
        except Exception as err:
            print(err,"Input must be a number from 1 to 5")
        else:
            break 
    return choice
        
#function that displays all of the inventory items
def display_all(dict_var):
    for key in dict_var:
        print(key)

#function that displays information about specific products
def display_item(dict_prices, dict_quantities):
    product = input('What is the name of the product?').capitalize()
    if product in dict_prices:
        print('Price: '+ dict_prices[product])
        print('Quantity: ' + dict_quantities[product])
    else:
        print("The product is not in the inventory.")

# function that allows the user to update an item
def update_item(dict_prices, dict_quantities):
    item = input("What is the name of the product?").capitalize()
    if item in dict_prices:
        update = input("What would you like to update? (options: Price, \
Quantiy, or Both)").capitalize()
        if update == 'Price':
            price_change = input('What is the updated price of ' + item 
                                 + '?')
            dict_prices[item] = price_change
        elif update == 'Quantity':
            quantity_change = input('What is the updated quantity of' + item +
'?')
        elif update == 'Both':
            price_change = input('What is the updated price of ' + item 
                                 + '?')
            dict_prices[item] = price_change
            quantity_change = input('What is the updated quantity of' + item +
'?')
            dict_quantities[item] = quantity_change
        else:
            print('The update must be either price, quantity or both.')
            update = input("What would you like to update? (options: Price, \
Quantiy, or Both)").capitalize()
    else:
        print('The product ' +item+ ' is not in the inventory')
 
# function that allows the user to input new inventory
def new_item(dict_prices, dict_quantities): 
    name = input("What is the name of the new item? ")
    price = input("What is the price of "+name +"? ")
    quantity = input("What is the available quantity of "+name +"? ")
    dict_prices[name] = price
    dict_quantities[name] = quantity
    
# main function that puts the program all together
def main():
    dict_prices = {}
    dict_quantities = {}
    read_file('initial_inventory.txt',dict_prices, dict_quantities)
    choice = get_user_choice()
    while choice != 5:
        if choice == 1:
            display_all(dict_prices)
        if choice == 2:
            display_item(dict_prices, dict_quantities)
        if choice == 3:
            new_item(dict_prices, dict_quantities)
        if choice == 4:
            update_item(dict_prices, dict_quantities)
        choice = get_user_choice()
    print('Program complete')
        
#Call main function
main()

