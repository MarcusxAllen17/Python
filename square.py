#Class header goes here

#ADD ANY NECESSARY IMPORT STATEMENTS HERE
import shape

#Define the Square class
#UPDATE TO INHERIT FROM SHAPE
class Square(shape.Shape):

    #Define the initializer method
    #UPDATE TO INCLUDE ARGUMENTS AND CALL INIT METHOD FROM SHAPE
    def __init__(self, new_border, new_name):
        
        #CALL INIT METHOD FROM SHAPE PASSING NECESSARY ARGUMENTS
        super().__init__(new_border, new_name)
        
        #DEFINE ATTRIBUTES SPECIFIC TO SQUARES; ASSIGN DEFAULT VALUES
         
        self.__side = 5
        
    def __str__(self):
        #CREATE STRING USING __str__ FROM SUPER AND ADD SIDE

        string = super().__str__() + '\nSide:' + str(self.__side)

        return string

    #Create accessor
    def get_side(self):
        return self.__side

    #Create mutator
    def set_side(self, new_side):
        if new_side > 0:
            self.__side = new_side
        else:
            print("Invalid side. Side not changed.")

    #Define calculate perimeter method
    def calc_perimeter(self):

        #Calculate perimeter
        perimeter = 4 * self.__side

        return perimeter

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = self.__side**2

        return area
