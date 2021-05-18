#Author: Marcus Allen
#Homework Number and Name: HW 4, Grade App
#Due Date: 3/12/2021
#Program Description: program that helps users compute their final grade

#Declare global constants
EXAM_1_Weight = .2
EXAM_2_Weight = .2
EXAM_3_Weight = .2
HOMEWORK_Weight = .3
FINAL_Weight = .1

#Define Function to query input
def get_grade(assignment_name):
    grade_input = float(input("What is your grade for " + assignment_name +"?"))
    while grade_input < 0 or grade_input > 100:
        print("The grade must be between 0 and 100, inclusive")
        grade_input = float(input("What is your grade for " + assignment_name +"?"))
    return grade_input

# Define function to calculate numeric average
def calc_average(exam_1, exam_2, exam_3, homework, final):
    avg = (exam_1*EXAM_1_Weight + exam_2*EXAM_2_Weight + exam_3*EXAM_3_Weight+
           homework*HOMEWORK_Weight + final*FINAL_Weight)
    return avg

#Define function to transform numeric average into letter grade
def calc_letter(average):
    if average >= 89.5:
        final_grade = 'A'
    elif average >= 79.5:
        final_grade = 'B'
    elif average >= 69.5:
        final_grade = 'C'
    elif average >= 59.5:
        final_grade = 'D'
    else:
        final_grade = 'F'
    return final_grade

# define main function
def main ():
    exam_1 = get_grade("exam 1")
    exam_2 = get_grade("exam 2")
    exam_3 = get_grade("exam 3")
    homework = get_grade('homework')
    final = get_grade('final project')
    
    avg = calc_average(exam_1, exam_2, exam_3, homework, final)
    
    final_grade = calc_letter(avg)
    
    print("Final Numeric Grade:", format(avg, '.2f' ))
    print("Final Letter Grade:", final_grade)

#Call main function
main()

































