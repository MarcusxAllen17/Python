# Marcus Allen and Emily Castaneda

# Defines the Inventory Class
class Inventory:
    
    # Defines the initializer for the class
    def __init__(self, new_id, new_name, new_price, new_stock):
        self.__id = new_id
        self.__name = new_name
        self.__price = new_price
        self.__stock = new_stock
    
    # Defines the Accessors
    def get_id(self):
        return self.__id 
    
    def get_name(self):
        return self.__name 
    
    def get_stock(self):
        return self.__stock 
    
    def get_price(self):
        return self.__price
    
    # Defines the Mutators
    def restock(self, new_quantity):
        if new_quantity*(-1) > 0:
            self.__stock = float(self.__stock) + float(new_quantity*(-1))
            self.__stock = str(self.__stock)
            return True
        else:
            return False
    
    def purchase(self, purch_qty):
        if float(self.__stock) - float(purch_qty) >= 0: 
            self.__stock = float(self.__stock) - float(purch_qty)
            self.__stock = str(self.__stock)
            return True
        else:
            return False
    
    # Defines the string function
    def __str__(self):
       return ((self.__id)  + 
               format(str(self.__name), '>30s')+ 
               format(str(self.__price), '>15s') + 
               format(str(self.__stock), '>15s'))
    
      
        
      
        
      
        
      
        
      
        
      
        
      