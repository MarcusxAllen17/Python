#Author: Marcus Allen
#Assignment Number: 8
#Date: 4/21/2021
#Description: program that calculates an individual's ROI

import calculation
import validation

def main():
    my_validation = validation.ValidationClass()
    
    initial_value = input("What is the initial value?")
    initial_value = my_validation.checkfloat(initial_value)
    
    current_value = input('What is the current value?')
    current_value = my_validation.checkfloat(current_value)

    my_calculation = calculation.CalculationClass()
    
    my_calculation.set_initial_value(initial_value)
    
    my_calculation.set_current_value(current_value)
    
    my_calculation.calc_ROI()
    
    ROI = my_calculation.get_ROI()*100
    
    print('The ROI for this investment is ' + format(ROI , '.2f') + '%')
    
main()