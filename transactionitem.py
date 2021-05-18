# Marcus Allen and Emily Castaneda

# Defiines the class
class TransactionItem():
    
    # Defines the initializer for the class
    def __init__(self, new_id, new_name, new_quantity, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__quantity = new_quantity
        self.__price = new_price
      
    # Defines the accessors for the class
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    
    
    
    # Defines the mutators for the class
    def set_id(self, new_id):
        self.__id = new_id
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_qty(self, new_qty):
        self.__quantity = new_qty
    
    def set_price(self, new_price):
        self.__price = new_price
    
    # Method calculates the cost of a particular item purchased
    def calc_cost(self):
        self.cost = float(self.__price) * float(self.__quantity)
        return self.cost
    
    # This is the string method
    def __str__(self):
        string = (str(self.__id) + 
                  format(str(self.__name), '>25s')
                  + format(str(self.__quantity), '>20s')
                  + format('$', '>12s')
                  + str(self.__price)
                  )
        return string
    
    
    