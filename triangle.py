#Class header goes here

#ADD ANY NECESSARY IMPORT STATEMENTS HERE
import shape

#Define the Triange class
#UPDATE TO INHERIT FROM SHAPE
class Triangle(shape.Shape):

    #Define the initializer method
    #UPDATE TO INCLUDE ARGUMENTS AND CALL INIT METHOD FROM SHAPE
    def __init__(self, new_border, new_name):
        #CALL INIT METHOD FROM SHAPE PASSING NECESSARY ARGUMENTS
        super().__init__( new_border, new_name)
        
        #DEFINE ATTRIBUTES SPECIFIC TO TRIANGLES; ASSIGN DEFAULT VALUES
        
        self.__height = 2
        
        self.__base = 1
        
    def __str__(self):
        #CREATE STRING USING __str__ FROM SUPER AND ADD BASE AND HEIG
        return (super().__str__() + '\nHeight:' +  str(self.__height) + 
                '\nBase'  + str(self.__base))  
    

    #Create accessor
    def get_base(self):
        return self.__base

    #Create mutator
    def set_base(self, new_base):
        if new_base > 0:
            self.__base = new_base
        else:
            print("Invalid base. Base not changed.")

    #Create accessor
    def get_height(self):
        return self.__height

    #Create mutator
    def set_height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Invalid height. Height not changed.")

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = 0.5 * self.__base + self.__height

        return area
