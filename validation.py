
class ValidationClass:
    
    #This method validates that the inputs are floats
    def checkfloat(self, str_input): 
        while True:
            try:
                return float(str_input)
            except ValueError:
                print('The input must be numeric')
                str_input = input('Please input the value again:')
             