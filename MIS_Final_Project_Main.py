# Marcus Allen and Emily Castaneda

import inventory 
import transactionitem


#function processes the inventory file into a dictionary 
def process_inventory(filename):
    object_dict = {}
    infile = open(filename, 'r')
    ID = infile.readline().strip()
    while ID != '':     
        Item = infile.readline().strip()
        Quantity = infile.readline().strip()
        Price = infile.readline().strip()
        object_dict[ID] = inventory.Inventory(ID, Item, Price, Quantity)
        ID = infile.readline().strip()
    infile.close()
    return object_dict
  
#function prints the menu for the customer
def print_inventory(object_dict):       
        print('ID',format('Item', '>30s'),format('Price', '>15s'),
              format('Qty Available', '>15s'))
        for x in object_dict:
            print(object_dict[x])
        print('Enter 0 when finished.')  
   
#function acquires the items the customer will buy or return  
def get_item_id(object_dict):
    name = ''
    transaction_dict = {}
    while name != '0':
        print_inventory(object_dict)
        name =input('Please input the item ID you would like to purchase or\
 return: ')
        if name in object_dict:
            quantity = float(input('What is the desired quantity? (Negative \
value for a return.):'))
            if quantity > 0:
                object_dict[name].purchase(quantity)
                ID = object_dict[name].get_id()
                Name = object_dict[name].get_name()
                Price = object_dict[name].get_price()
                transaction_dict[ID] = transactionitem.TransactionItem(ID, Name
, quantity, Price)
                transaction_dict[ID].calc_cost
                if object_dict[name].purchase(quantity) == False:
                    print("Sorry, we don't have enough in stock")
            elif quantity < 0:
                object_dict[name].restock(quantity)
                ID = object_dict[name].get_id()
                Name = object_dict[name].get_name()
                Price = object_dict[name].get_price()
                transaction_dict[ID] = transactionitem.TransactionItem(ID, Name
, quantity, Price)
                transaction_dict[ID].calc_cost()
        elif name == '0':
            print('Program complete')
            break
        else:
            print('Input was invalid')
           
    return object_dict, transaction_dict

def print_invoices(transaction_dict):
    if len(transaction_dict) != 0:
        print('ID' + 
        format('Item', '>25s' ) +
        format('Quantity', '>20s') +
        format('Price', '>17s' )+ 
        format('Total', '>13s'))
        for x in transaction_dict:
            cost = transaction_dict[x].calc_cost()
            print(transaction_dict[x], format('$', '>10s'),str(cost),
                      sep ='')
        
        Price = 0
        for ID in transaction_dict:
            Price = transaction_dict[ID].calc_cost() + Price
            
        Tax = .085*Price
        Total = Price + Tax
        print('')
        print('Price: $', format(Price, ',.2f'), sep ='')
        print('Tax: $', format(Tax, ',.2f'), sep ='')
        print('Total: $', format(Total, ',.2f'), sep ='')
    else:
        print('Thank you for visiting!')
     
#function writes the updated inventory into a new file  
def new_file(file_name, new_dict):
    infile = open(file_name, 'w')
    for x in new_dict:
        ID = new_dict[x].get_id()
        Name = str(new_dict[x].get_name())
        Stock = str(new_dict[x].get_stock())
        Price = str(new_dict[x].get_price())
        infile.write( str(ID) + '\n')
        infile.write( Name +'\n')
        infile.write(Stock + '\n')
        infile.write( Price +  '\n')      

#function puts the whole program together  
def main():
    object_dict = process_inventory('inventory.txt')
    new_dict = get_item_id(object_dict)
    new_file('UpdatedInventory.txt', new_dict[0])
    print_invoices(new_dict[1])


main()
