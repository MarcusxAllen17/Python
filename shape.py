#Class header goes here

#Define the Shape class
class Shape:

    #Define the initializer method
    def __init__(self, border, name):
        self.__color = 'blue'
        self.__border = border
        self.__name = name
        #define attributes of each Shape object with starting values
        #Make sure border is positive before setting the border value

    #Create Mutators
    def set_color(self, new_color):
        self.__color = new_color
        
    def set_border(self, new_border):
        self.__border = new_border
        
    def set_name(self, new_name):
        self.__name = new_name

    #Create accessors
    def get_border(self):
        return self.__border

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def __str__(self):
        string = (self.__name + " \nColor: " + self.__color + " \nBorder: " + 
                  str(self.__border))
        return string
