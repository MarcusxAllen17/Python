class CalculationClass:
    
    # Here are the Mutators for the initial and current values
    def set_initial_value(self, value1):
        self.__initial_value = value1
        
    def set_current_value(self, value2):
        self.__current_value = value2
       
    # This method calculates the ROI
    def calc_ROI(self):
        self.__ROI = ((self.__current_value-self.__initial_value)/
                      self.__initial_value)
        
    # This is the Accessor for the ROI
    def get_ROI(self):
        return self.__ROI
